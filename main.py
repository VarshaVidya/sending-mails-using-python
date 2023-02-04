import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 5:

    file = open("quotes.txt")
    contents = file.read()
    contents_list = contents.split("\n")
    random_quote = random.choice(contents_list)
    my_email = "sampleuse02@gmail.com"
    password = "aynzpeosvaozhhtc"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="sampleuse01@yahoo.com",
                        msg=f"Subject:Monday quote\n\n{random_quote} ")
    connection.close()
    file.close()
# print(random.choice(list(open('file.txt'))))

