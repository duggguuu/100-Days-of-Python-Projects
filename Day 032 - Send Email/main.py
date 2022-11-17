import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL="yashistestingbigtime@gmail.com"
MY_PASSWORD="zqoetrgfpknlhmbs"

today=dt.datetime.now()
today_data=(today.month,today.day)

bdays=pandas.read_csv("birthdays.csv")
bday_dict={(data_row.month,data_row.day):data_row for (index,data_row) in bdays.iterrows()}


if (today_data) in bday_dict:
    bday_person=bday_dict[today_data]
    letter_path=f"letters/letter_{random.randint(1,3)}.txt"
   
    with open(letter_path) as letter_file:
        contents=letter_file.read()
        x=contents.replace("[NAME]",bday_person["Name"])
  
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls()
        server.login(MY_EMAIL,MY_PASSWORD)
        server.sendmail(from_addr=MY_EMAIL,to_addrs=bday_person["email"],msg=f"Subject:HBD!!\n\n{x}")