import smtplib
my_email="mithumoger8@gmail.com"
password="23/04/2002"
connection=smtplib.SMTP("smtp.gmail.com",port=587)
connection.login(user=my_email,password=password)


import random
with open("quotes.txt") as file:
    text=file.read()
    quotes=text.split("\n")
    quote=random.choice(quotes)




import datetime as dt
now=dt.datetime.now()
if datetime.datetime.now().weekday() == 3:  # 3 corresponds to Thursday
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="mithilesh661@yahoo.com", msg=f"Subject:Monday quote\n\n{quote}")
        connection.close()
print(quote)