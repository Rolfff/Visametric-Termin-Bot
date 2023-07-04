#!/usr/bin/env python
#
install = {
    "isLinux": False,
    "LINUX_GECKOPATH":"/usr/local/bin/geckodriver",
    "WINDOWS_GECKOPATH": "C:\\path\\to\\geckodriver.exe",
    "win_binary_location": r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe',
    "LOGFILE": "./Visametric.log"
}

legalization = {
    "landing_page" : "https://ir-appointment.visametric.com/de",
    "first_form": {
         "city" :"TEHERAN",
         "office" : "TEHERAN", 
         "officetype" : "NORMAL",
         "totalPerson" : "1 Antragsteller",
         "Zahlungsart":"Karten- und mobile Zahlung", 
         "paymentCardInput":"000000000",
         "date":"1401/10/08",
        },
    "second_form":{
        "scheba_number" : "0000000",
        "scheba_name" : "Persish letters!!!!",
        "name1" : "NAME",
        "surname1" : "SURNAME",
        "birthday1" : "01",
        "birthmonth1" : "01",
        "birthyear1" : "1955",
        "passport1" : "",
        "phone1" : "091",
        "phone21" : "091",
        "email1" : "test@gmail.com" ,
    }


}
