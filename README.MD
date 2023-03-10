# Selenium Visametric Termin Bot

This Python Selenium script helps to find available dates for legalization of documents by the [German Embassy](https://teheran.diplo.de/) in Tehran. 
The script only helps to enter the personal data. You need to solve the Google Recaptcha for each operation.

## Notes
- It is tested and developed January 2023. When the page is rebuilt, the script should be adjusted.
- The Script does not check the Transaction ID. It takes the first one.
- The Script take the first found time slot and stops.


https://ir-appointment.visametric.com/de/

## Install
First install Python3 on your system. 
Then:
- pip install -U selenium
- pip install fake-useragent

Optional for linux:
- sudo apt install speech-dispatcher



