#Quelle: https://selenium-python.readthedocs.io/

#!/usr/bin/env python
import config as c

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
from datetime import datetime
from pathlib import Path
import random
import time
import os
import logging

GECKOPATH = c.install["LINUX_GECKOPATH"]

logging.basicConfig(filename=c.install["LOGFILE"], level=logging.INFO)

OKGREEN = '\033[92m'                                                            
OKBLUE = '\033[94m'                                                             
ENDC = '\033[0m'                                                                
BOLD = "\033[1m"                                                                
                                                                                
HEADER = '\033[95m'                                                             
WARNING = '\033[93m'                                                            
FAIL = '\033[91m'                                                               
           
class Output:

    def warn(self, message):
        print('\t' + WARNING + message + ENDC+'\n')
    def error(self, message):
        print('\t' + FAIL + message + ENDC+'\n')
    def info(self, message):
        print('\t' + OKBLUE + message + ENDC+'\n') 
    def success(self, message):
        print('\t' + OKGREEN + message + ENDC+'\n') 
    def passed(self, message):
        print('\t' + BOLD + message + ENDC+'\n') 
    def header(self, message):
        print('\t' + HEADER + message + ENDC+'\n')         
        
class Search:

    def __init__(self):
        self.url = "http://www.python.org"
        options = Options()
        if not c.install["isLinux"]:
            options.binary_location = c.install["win_binary_location"]
            GECKOPATH = c.install["WINDOWS_GECKOPATH"]
        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)
        options.add_argument(f'user-agent={userAgent}')
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        self.driver = webdriver.Firefox(capabilities=cap, options=options, firefox_profile=firefox_profile, executable_path=GECKOPATH)
        self.driver.get(self.url)
   

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert 'Python' in driver.title
        elem = driver.find_element(By.NAME, 'q')
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        #el = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"p"))
        #assert el.text == "Hello from JavaScript!"
        assert "No results found." not in driver.page_source
        
    def getTerminByVisametric(self):
        out = Output()
        driver = self.driver
        driver.get(c.legalization['landing_page'])
        try:
            assert 'Visametric - Visa Application Center' in driver.title
        except AssertionError:
            if c.install["isLinux"]:
                os.system('spd-say "Error. Page not found!"')
            out.error("Error. Page not found!")
            logging.error(str(datetime.now())+" Page not found: "+c.legalization['landing_page'])
            return None

        #Push Button name="legalizationBtn" 
        elem = driver.find_element(By.NAME, 'legalizationBtn')
        elem.click()
        #Check OK Radio-Input name="surveyStart" id="result0"
        elem = driver.find_element(By.ID, 'result0')
        elem.click()
        #Check Iran Radio-Input name="nationality" id="result1"
        WebDriverWait(driver, random.randint(5,25)).until(
                    EC.element_to_be_clickable((By.ID, 'result1'))
                )
        elem = driver.find_element(By.ID, 'result1')
        elem.click()
        # Captcha Part id="recaptcha-anchor"
        WebDriverWait(driver, random.randint(10,25)).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]"))
            )
        element = WebDriverWait(driver, random.randint(10,25)).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-checkmark"))
            )
        driver.execute_script("arguments[0].click();", element)
        current_url = driver.current_url
        elem = driver.find_element(By.ID, 'recaptcha-anchor')
        while elem.get_attribute("aria-checked") == 'false' :
            if c.install["isLinux"]:
                os.system('spd-say "Waiting for human interaction."')
            out.warn("Please resolve the captcha or press 'str+c' ")
            out.warn('Waiting for human interaction.')
            time.sleep(10) # Delay for 10 seconds.
        out.info('captcha done')
        
        driver.switch_to.default_content()
        #To ignore google recaptcha
#        driver.execute_script("$('#formAccessApplication').submit();")
        driver.find_element(By.ID, 'btnSubmit').click()

        
        while current_url == driver.current_url:
            try:
                WebDriverWait(driver, random.randint(10,25)).until(EC.url_changes(current_url))
            except:
                out.warn("Please push the blue button. ")
        time.sleep(2) # Delay for 2 seconds.
        
        
        #Select input id="city"
        select = Select(WebDriverWait(driver, random.randint(10,25)).until(
                EC.presence_of_element_located((By.ID, 'city'))
            ))
        
        
        #select = Select(driver.find_element(By.ID, 'city'))
        select.select_by_visible_text(c.legalization["first_form"]['city'])
        #Select input id="office"
        select = Select(driver.find_element(By.ID, 'office'))
        select.select_by_visible_text(c.legalization["first_form"]['office'])
        #Select input id="officetype"
        select = Select(driver.find_element(By.ID, 'officetype'))
        select.select_by_visible_text(c.legalization["first_form"]['officetype'])
        #Select input id="totalPerson"
        select = Select(driver.find_element(By.ID, 'totalPerson'))
        select.select_by_visible_text(c.legalization["first_form"]['totalPerson'])
        #Check ATM Radio-Input id="atm"
        WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, 'atm'))
                )
        elem = driver.find_element(By.ID, 'atm')
        elem.click()
        #Input Cardnumber id="paymentCardInput"
        WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, 'paymentCardInput'))
                )
        elem = driver.find_element(By.ID, 'paymentCardInput')
        elem.send_keys(c.legalization["first_form"]['paymentCardInput'])
        
         #id="popupDatepicker2"
        elemDatePicker = driver.find_element(By.ID, 'popupDatepicker2')
        driver.execute_script("arguments[0].removeAttribute('readonly')", WebDriverWait(driver, 20).until(EC.element_to_be_clickable(elemDatePicker)))
        elemDatePicker.clear()
        elemDatePicker.send_keys(c.legalization["first_form"]['date'])
        elem.click()
        #Button id="checkCardListBtn"
        driver.find_element(By.ID, 'checkCardListBtn').click()
        #Check  Radio-Input name="bankpayment"
        WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.NAME, 'bankpayment'))
                ).click()
#        try:
#            assert 'Visametric - Visa Application Center' in driver.title
#        except AssertionError:
        current_url = driver.current_url
        #button id="btnAppCountNext"
        driver.find_element(By.ID, 'btnAppCountNext').click()

#        while current_url == driver.current_url:
#            try:
#                WebDriverWait(driver, random.randint(10,25)).until(EC.url_changes(current_url))
#            except:
#                out.warn("Please push the blue button. ")
        time.sleep(2) # Delay for 2 seconds.
        
        #input id="scheba_number"
        elem = WebDriverWait(driver, random.randint(10,25)).until(
                EC.presence_of_element_located((By.ID, 'scheba_number'))
            )
        elem.send_keys(c.legalization["second_form"]['scheba_number'])
        #input id="scheba_name" in persian letters!!!!
        driver.find_element(By.ID, 'scheba_name').send_keys(c.legalization["second_form"]['scheba_name'])
        #input id="name1"
        driver.find_element(By.ID, 'name1').send_keys(c.legalization["second_form"]['name1'])
        #input id="surname1"
        driver.find_element(By.ID, 'surname1').send_keys(c.legalization["second_form"]['surname1'])
        #Select input id="birthday1"
        select = Select(driver.find_element(By.ID, 'birthday1'))
        select.select_by_visible_text(c.legalization["second_form"]['birthday1'])
        #Select input id="birthmonth1"
        select = Select(driver.find_element(By.ID, 'birthmonth1'))
        select.select_by_visible_text(c.legalization["second_form"]['birthmonth1'])
        #Select input id="birthyear1"
        select = Select(driver.find_element(By.ID, 'birthyear1'))
        select.select_by_visible_text(c.legalization["second_form"]['birthyear1'])
        #input id="passport1"
        driver.find_element(By.ID, 'passport1').send_keys(c.legalization["second_form"]['passport1'])
        #input id="phone1"
        driver.find_element(By.ID, 'phone1').send_keys(c.legalization["second_form"]['phone1'])
        #input id="phone21"
        driver.find_element(By.ID, 'phone21').send_keys(c.legalization["second_form"]['phone21'])
        #input id="email1"
        driver.find_element(By.ID, 'email1').send_keys(c.legalization["second_form"]['email1'])
        
        #link id="btnAppPersonalNext"
        current_url = driver.current_url
        #button id="btnAppPersonalNext"
        driver.find_element(By.ID, 'btnAppPersonalNext').click()
        #checkbox id="previewchk"
        elem = WebDriverWait(driver, random.randint(10,25)).until(
                EC.presence_of_element_located((By.ID, 'previewchk'))
            )
        elem.click()
        #button id="btnAppPreviewNext"
        driver.find_element(By.ID, 'btnAppPreviewNext').click()
        
        time.sleep(2) # Delay for 2 seconds.
        
        elem = WebDriverWait(driver, random.randint(10,25)).until(
                EC.presence_of_element_located((By.ID, 'datepicker'))
            )
        elem.click()

        #driver.switch_to.frame(driver.find_elements(By.CSS_SELECTOR,"div .datepicker-days"))
        foundTermin = False
        countMonth = 0
        while countMonth < 3:
            dayElems = driver.find_elements(By.CSS_SELECTOR,".day")
            monthElem = driver.find_element(By.CSS_SELECTOR,'.datepicker-switch').get_attribute('innerHTML')
            for dayElem in dayElems:
                value = dayElem.get_attribute('innerHTML')
     
                if "disabled" in dayElem.get_attribute('class'):
                    #print (value +" "+monthElem+" Element is not clickable")
                    i = 0
                else:
                    dayElem.click()
                    print (value +" "+monthElem+" Element is clickable")
                    foundTermin = True
                    break
                #For end
            if foundTermin:
                break
            #Next Month Button
            #<th class="next" style="visibility: visible;">»</th>
            if countMonth < 2:
                driver.find_element(By.CSS_SELECTOR, '.next').click()
            countMonth += 1
            #While End
        if foundTermin:
            #button id= btnAppCalendarNext
            driver.find_element(By.ID, 'btnAppCalendarNext').click()
            out.success(str(datetime.now())+" Es wurde ein Termin gefunden!!!!")
            logging.info(str(datetime.now())+" Es wurde ein Termin gefunden!!!!")
        else: 
            out.info(str(datetime.now())+" Leider keine Termine gefunden.")
            logging.info(str(datetime.now())+" Leider keine Termine gefunden.")
        return foundTermin
                
        
        


        
        #to refresh the browser
        #driver.refresh()
        # Zeit Element -> id="watch"
        #<span id="watch"><b>7m 6s </b></span>
        
        #Abgelaufener Tag
#<td class="old disabled day disabled">28</td>
#TZoday
#<td class="today disabled day disabled">14</td>
                #disabled Day
#        <td class="day disabled">19</td>
        #tag nächster Monat
       # <td class="new day disabled">1</td>
        
        


    def tearDown(self):
        self.driver.close()
    

        
        

if __name__ == "__main__":
    termin = False
    
    while termin == False:
        s = Search()
        termin = s.getTerminByVisametric()
        if termin == None:
            termin = False
            time.sleep(5) # Delay for 5 seconds.
        if not termin:
            s.tearDown()
            del(s)
#    s.test_search_in_python_org()
#    s.tearDown()
