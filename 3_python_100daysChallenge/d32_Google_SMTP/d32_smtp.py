import smtplib
my_mail = "fangsihyu0211@gmail.com"
password = "ugmoomuqmjnrhynd"


with smtplib.SMTP("smtp.gmail.com") as connection:
    # connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail,
                        to_addrs="nickmomo1524@gmail.com", 
                        msg="Subject:Hello\n\nthe body of the email")
    # connection.close()
    # by using "with", there is no need using "connection.close()", the same trick at open file

# 291.___________________________________________________
import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now,year,month,day_of_week)

data_of_birth = dt.datetime(year=2000, month=2, day=11, hour=12)
print(data_of_birth)

# 292.___________________________________________________

import smtplib
import datetime as dt
import random

my_mail = "fangsihyu0211@gmail.com"
password = "ugmoomuqmjnrhynd"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    #  beaware the condition
    with open ("3_python_100daysChallenge/d32_Google_SMTP/quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs="nickmomo1524@gmail.com", 
                            msg=f"Subject:Quote\n\nthe body of the email\n{quote}")
        
