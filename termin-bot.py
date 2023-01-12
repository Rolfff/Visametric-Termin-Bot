#Quelle: https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from csv import writer
from csv import reader
from pathlib import Path
import time

class Search:

    def __init__(self):
        self.url = "https://scholar.google.de/"
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

        

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        
    def search(self, text):
        counter = 0
        value = ""
        zitateURL = ""
        driver = self.driver
#        element = driver.find_element_by_id("gs_hdr_tsi")
        element = driver.find_element_by_name("q")
        element.clear()
        # save current page url
        current_url = driver.current_url
        driver.implicitly_wait(2) # seconds
        element.send_keys(text, Keys.RETURN)
        # wait for URL to change with 15 seconds timeout
        WebDriverWait(driver, 15).until(EC.url_changes(current_url))
        isCaptcha = 1
        while isCaptcha == 1:
            try:
                captcha = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.ID, 'gs_captcha_f'))
                )
                print("Captcha entdeckt")
                # taking input from the user
                print("Nochmal versuchen? (y/n)")
                a = input()
                # printing the data
                print("User data:-", a)
                if a == "y":
                    isCaptcha = 1
                else:
                    isCaptcha = 0 
                    return "null"
            except (NoSuchElementException, TimeoutException) as e:
                isCaptcha = 0 
                print("Kein Captcha entdeckt")
               
               
               
               
#        while isCaptcha == 1:
        try:
            zitiert_link = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Zitiert von:'))
            )
    #       zitiert_link = driver.find_element_by_partial_link_text('Zitiert von:')
            value = zitiert_link.get_attribute('innerHTML')
            counter = value[13:] #Entfernt 'Zitiert von: ' vor der Zahl
            zitateURL = zitiert_link.get_attribute('href')
#            isCaptcha = 0
        except (NoSuchElementException, TimeoutException) as e:
            counter = 0
            print (text+" No Link found.")
#            element.clear()
#            isCaptcha = 1
            counter = 0
            zitateURL = ""
        return [str(counter), str(zitateURL)]

    def tearDown(self):
        self.driver.close()
        
class CSVHandler():
    def __init__(self, csvFile, newCsvFile):
        self.csvFile = csvFile
        self.newCsvFile = newCsvFile
    
    def run(self, zeile):
        my_file = Path(self.newCsvFile)
        line_finished = 0
        if my_file.is_file(): #Wenn Datei existert
            with open(self.newCsvFile, mode='r') as read_obj:
                csv_reader = reader(read_obj)
                line_finished = sum(1 for row in csv_reader)
        print(str(line_finished) +" Zeilen übersprungen")
        
        s = Search()
        with open(self.csvFile, mode='r') as read_obj, \
                open(self.newCsvFile, 'a', newline='') as write_obj:
            # Create a csv.reader object from the input file object
            csv_reader = reader(read_obj)
            # Create a csv.writer object from the output file object
            csv_writer = writer(write_obj)
            # Read each row of the input csv file as list
            line_count = 0
            for x in range(line_finished):
                next(csv_reader)
            for row in csv_reader:
                if line_count == 0 and line_finished == 0:
                    print(f'Column names are {", ".join(row)}')
                    # Append the default text in the row / list
                    row.append("Anz Zitate Google")
                    row.append("Link zu Zitate Google")
                else:
                    value = s.search(row[zeile])
                    if value == "null":
                        break
                    #print("Suche: "+row[zeile]+ " A:"+ value[0] +" URL: "+ value[1])
                    print("Suche: "+row[zeile]+ " Zitate:"+ value[0])
                    # Append the default text in the row / list
                    row.append(value[0]) #Zitate Anzahl
                    row.append(value[1]) #Zitate Link
                # Add the updated row / list to the output file
                csv_writer.writerow(row)  
                print("Write in row "+ str(line_count+line_finished))
                line_count += 1
            print(f'Processed {line_count} lines.')
        s.tearDown()
        
        

if __name__ == "__main__":
    csvFile = "IEEE_export2020.10.30-12.50.39.csv"
    NewCsvFile = "Google_IEEE_export_2020.10.30-12.50.39.csv"
    proz = CSVHandler(csvFile,NewCsvFile);
    proz.run(13)
#    s = Search()
#    ret = s.search("10.1007/978-3-642-39354-9_35")
#    print(ret[13:])
#    s.tearDown()
