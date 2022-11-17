import requests
import datetime as dt
import smtplib
import time

MYLAT=22.804565
MYLONG=86.202873

MY_EMAIL="yashistestingbigtime@gmail.com"
MY_PASSWORD="zqoetrgfpknlhmbs"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(MY_EMAIL,MY_PASSWORD)

isspos=requests.get("http://api.open-notify.org/iss-now.json")
isspos.raise_for_status()
iss_data=isspos.json()
lats=float(iss_data["iss_position"]["latitude"])
longs=float(iss_data["iss_position"]["longitude"])

while True:
    time.sleep(60)
    
    if lats>MYLAT-5 and lats<MYLAT+5 and longs>MYLONG-5 and longs<MYLONG+5:

        y=str(dt.datetime.now().year)
        m=str(dt.datetime.now().month)
        d=str(dt.datetime.now().day)
        datenow=y+"-"+m+"-"+d
        h=dt.datetime.now().hour

        paras={"lat":MYLAT,"long":MYLONG,"date":datenow,"formatted":0}
        mypos=requests.get("http://api.sunrise-sunset.org/json",params=paras)
        mypos.raise_for_status()
        data=mypos.json()
        sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
        
        if h==sunset:
            server.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Where's the ISS??\n\nLook up!!!!!!")
            server.quit()

    else:
        server.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Where's the ISS??\n\nGo to sleep!!!!!!")
        server.quit()