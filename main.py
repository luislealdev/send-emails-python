import smtplib
import datetime as dt
import random

email = "hereyouremail@gmail.com"
secure_password = "your_google_auth_password"

day = dt.datetime.now().weekday()   
if(day==5):
    with open("quotes.txt") as quotes:
        quote = random.choice(quotes.readlines())

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=secure_password)
            connection.sendmail(
                from_addr=email,
                to_addrs="carolinamtz091@gmail.com",
                msg=f"Subject:HEY! Tu frase del dia\n\n{quote}"
            )
