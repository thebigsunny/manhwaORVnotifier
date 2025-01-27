# Manhwa Chapter Notifier

![Kim Dokja](kimdokja.jpg)

A Python script that automatically checks for new chapters of "Omniscient Reader's Viewpoint" and sends SMS notifications when new chapters are available.

## Requirements
- Python 3.x
- Chrome browser
- Required packages listed in `requirements.txt`

## Setup
1. Clone the repository
2. Create a virtual environment: `python3 -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Update the phone number in `main.py`
6. Run the script: `python main.py`

## Features
- Checks for new chapters every 3 hours
- Sends SMS notifications with chapter link
- Automatically manages browser sessions