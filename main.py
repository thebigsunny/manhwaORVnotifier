import requests 
import schedule 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

lastChapter = None

def getChapter():
    driver = webdriver.Chrome()
    driver.get("https://mangakatana.com/manga/omniscient-readers-viewpoint.24674")
    chapter = driver.find_element(By.CLASS_NAME, "d-cell-small value new_chap")
    driver.quit()
    chapter_text = chapter.text
    chapter_number = ''.join(filter(str.isdigit, chapter_text))
    return chapter_text, chapter_number

def checkAndSendMessage():
    global lastChapter
    current_chapter, chapter_number = getChapter()
    
    # Only send message if chapter has changed
    if current_chapter != lastChapter:
        chapter_url = f"https://mangakatana.com/manga/omniscient-readers-viewpoint.24674/c{chapter_number}"
        resp = requests.post('https://textbelt.com/text', {
            'phone': '832-951-9801',
            'message': f'New chapter available: {current_chapter}\nRead here: {chapter_url}',
            'key': 'textbelt',
        })
        lastChapter = current_chapter

schedule.every(3).hours.do(checkAndSendMessage)

checkAndSendMessage()

while True:
    schedule.run_pending()
    time.sleep(1)





