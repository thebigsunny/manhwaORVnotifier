import requests 
import schedule 
import time
from credentials import phoneNumber
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

lastChapter = None

def getChapter():
    # using selenium to get the chapter number from the website

    driver = webdriver.Chrome()
    driver.get("https://mangakatana.com/manga/omniscient-readers-viewpoint.24674")
    chapter = driver.find_element(By.CLASS_NAME, "d-cell-small value new_chap")
    driver.quit()
    chapterText = chapter.text

    # filters through the chapterText, only gets the digits, then joins them together without spaces
    chapterNumber = ''.join(filter(str.isdigit, chapterText))
    return chapterText, chapterNumber

def checkAndSendMessage():

    # so that it refers to the global, overarching, lastChapter variable
    global lastChapter

    # getting the variables we are chechking for
    currentChapter, chapterNumber = getChapter()
    
    if lastChapter == None or currentChapter != lastChapter:
        chapterUrl = f"https://mangakatana.com/manga/omniscient-readers-viewpoint.24674/c{chapterNumber}"
        resp = requests.post('https://textbelt.com/text', {
            'phone': phoneNumber,
            'message': f'New chapter available: {currentChapter}\nRead here: {chapterUrl}',
            'key': 'textbelt',
        })

        lastChapter = currentChapter

schedule.every(3).hours.do(checkAndSendMessage)

checkAndSendMessage()

# checking to see if the 3 hour time period to run checkAndSendMessage is over 

while True:
    schedule.run_pending()
    time.sleep(5)
