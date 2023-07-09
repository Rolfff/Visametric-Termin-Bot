# Selenium Visametric Termin Bot

This Python Selenium script helps to find available dates for legalization of documents by the [German Embassy](https://teheran.diplo.de/) in Tehran. 
The script **only helps to enter your personal data**. You need to solve the Google Recaptcha for each operation.

## Ethnic note
This script should help Iranian citizens to get an appointment at Visametric in the foreseeable future without having to spend a lot of money on the black market. It gives them the opportunity to work with similar or the same weapons as the appointment traders. 
Additionally, it can be used to document the appointment method of the German Embassy in Tehran and collect evidence for future complaints or court proceedings. 

## Notes
- It is tested and developed January 2023. When the page is rebuilt, the script should be adjusted.
- The Script does not check the Transaction ID. It takes the first one.
- The Script take the first found time slot and stops.
- At the moment it works only if you have paid with card the Visametirc deposit.
- The bot works with the german formular https://ir-appointment.visametric.com/de/ (You are invited to extend the script to other languages.)

## Install
1. First install [Python3](https://www.python.org/downloads/) on your system. 
- For Windows at the [Microsoft Store](https://www.microsoft.com/store/productId/9NJ46SX7X90P)
2. [Run Python3 in command prompt](https://www.youtube.com/watch?v=pFYcAOsNyvs)
3. [Installing Python3 packages](https://packaging.python.org/en/latest/tutorials/installing-packages/): 
Copy and paste the following lines into the command prompt.

```sh
pip install -U selenium
pip install fake-useragent
pip install undetected-chromedriver
```
4. Install [Google Chrome](https://www.google.com/intl/de_de/chrome/) on your system. Make sure that Chrome runs without problems on your system.

Optional for linux:
- ```sudo apt install speech-dispatcher```


## Usage
1. [Downloard this script](https://github.com/Rolfff/Visametric-Termin-Bot/archive/refs/heads/master.zip).
2. Rename the 'config_example.py' file to 'config.py'
3. Fill [config_example.py](./config_example.py) with your data.
4. Open the command prompt at the location from the downloaded files and run ```python3 ./termin-bot.py```
5. Answer the captcha and wait. Good luck!
6. If you want to help improve the situation for others, share your log file (see ```"LOGFILE": "./Visametric.log"``` path at your config.py) with us. We will document it [here](./log_history/).



## Contribute
open an [Issue](https://github.com/Rolfff/Visametric-Termin-Bot/issues) fore questions or bugs. Or you can fix it yourself and create a change request. 
