import requests
from datetime import datetime
import smtplib
import time

MY_LATI = 25.026270
MY_LONGTI = 121.418538

my_mail = "fangsihyu0211@gmail.com"
password = "ugmoomuqmjnrhynd"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_ISS = response.json()

    iss_lat = float(data_ISS["iss_position"]["latitude"])
    iss_long = float(data_ISS["iss_position"]["longitude"])

    if MY_LATI-5<=iss_lat<=MY_LATI+5 and MY_LONGTI-5<=iss_long<=MY_LONGTI+5:
        return True


def is_night():
    parameters = {"lat":MY_LATI, 
                "lng":MY_LONGTI,
                "formatted":0}

    response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_SUN = response_sun.json()
    sunset = int(data_SUN["results"]["sunrise"].split("T")[1].split(":")[0])
    sunrise = int(data_SUN["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now>= sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=my_mail, 
                msg="Subject:Look up the sky!\n\nISS is above you in the sky!")
            



