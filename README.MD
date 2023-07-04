# Selenium Visametric Termin Bot

This Python Selenium script helps to find available dates for legalization of documents by the [German Embassy](https://teheran.diplo.de/) in Tehran. 
The script **only helps to enter your personal data**. You need to solve the Google Recaptcha for each operation.

## Notes
- It is tested and developed January 2023. When the page is rebuilt, the script should be adjusted.
- The Script does not check the Transaction ID. It takes the first one.
- The Script take the first found time slot and stops.


https://ir-appointment.visametric.com/de/

## Install
1. First install [Python3](https://www.python.org/downloads/) on your system. 
2. [Run Python3 in command prompt](https://www.youtube.com/watch?v=pFYcAOsNyvs)
- For Windows at the [Microsoft Store](https://www.microsoft.com/store/productId/9NJ46SX7X90P)
3. [Installing Python3 packages](https://packaging.python.org/en/latest/tutorials/installing-packages/): 
Copy and paste the following lines into the command prompt.

```sh
pip install -U selenium
pip install fake-useragent
```
4. Install [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) on your system. Make sure that Firefox runs without problems on your system.
5. Download the [geckodriver](https://github.com/mozilla/geckodriver/releases) for your system and unzip it. (For Windows use 'geckodriver-v0.33.0-win32.zip'.) 

Optional for linux:
- ```sudo apt install speech-dispatcher```


## Usage
1. [Downloard this script](https://github.com/Rolfff/Visametric-Termin-Bot/archive/refs/heads/master.zip).
2. Fill [config_example.py](https://github.com/Rolfff/Visametric-Termin-Bot/blob/master/config_example.py) with your data.

- For Windows systems:
  - Edit path to Firefox binary ```"win_binary_location": r'C:\Program Files\Mozilla Firefox\firefox.exe'```
  - Edit path to geckodriver (see Install step 5) ```"WINDOWS_GECKOPATH": "C:\\path\\to\\geckodriver.exe"``` for windows. (please use ```\\``` for ```\```.)
- For Linux systems:
  - switch ```"isLinux": False"``` to True.
  - Edit path to geckodriver (see Install step 5) ```"LINUX_GECKOPATH":"/usr/local/bin/geckodriver"```.

3. Rename the 'config_example.py' file to 'config.py'
4. Open the command prompt at the location from the downloaded files and run ```python3 ./termin-bot.py```
5. Answer the Google captcha and wait. Good luck!

## Troubleshooting
If you get this message:
-  ```ModuleNotFoundError: No module named 'config'```: You did not rename the config file. See point 3 at topic "Usage".
- ```ModuleNotFoundError: No module named 'selenium'```: You did not install selenium. See point  3 at topic "Install".
- ```ModuleNotFoundError: No module named 'fake_useragent'```: You did not install fake_useragent. See point  3 at topic "Install".
- ```selenium.common.exceptions.InvalidArgumentException: Message: binary is not a Firefox executable```: The path to the firefox.exe is not right. See point 2 at topic "Usage".



## Contribute
open an [Issue](https://github.com/Rolfff/Visametric-Termin-Bot/issues) fore questions or bugs. Or you can fix it yourself and create a change request. 
