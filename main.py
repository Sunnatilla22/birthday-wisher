##################### Extra Hard Starting Project ######################
import smtplib

import pandas as pd
import datetime as dt
import random

my_email = "mirvaliyevsunnat@gmail.com"
password = "bkqkhmxfnsrgvkox"


# 1. Update the birthdays.csv
birthday_data = pd.read_csv("birthdays.csv")

# print(birthday_data)
new_data = {
    'name': ["Carl", "Hayrulla", "Adam"],
    "email": ["carljameson591@gmail.com", "hayrullamirvaliyev@gmail.com","adam@gmail.com"],
    "year": [2022, 2022, 2000],
    "month":[12, 12, 12],
    "day": [24, 24, 10]
}

df = pd.DataFrame(new_data)
# df.to_csv("birthdays.csv", mode="a", index=False, header=False)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)
birthday_dict = {(data_row["month"], data_row["day"]):data_row for
                 (index, data_row) in birthday_data.iterrows()}
# birthday_dict = {(data_row["month"], data_row["day"]):",".join((data_row["name"],
#                  data_row["email"], str(data_row["year"]), str(data_row["month"]), str(data_row["day"]))) for
#                  (index, data_row) in birthday_data.iterrows()}
# print(birthday_dict)
# for (index, data_row) in birthday_data.iterrows():
    # print(data_row["month"])
    # print(data_row["day"])

if today in birthday_dict:
    print(birthday_dict[today])
    birthday_person = birthday_dict[today]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        letter_content = letter.read()
        new_letter = letter_content.replace("[NAME]", birthday_person["name"])
        print(new_letter)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        # with open(f"./letter_templates/letter_{random_num}.txt", mode="w") as completed_letter:
        #     complete = completed_letter.write(new_letter)
        #     print(completed_letter)


# 4. Send the letter generated in step 3 to that person's email address.
if today_month == 12 and today_day == 25:
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{new_letter}")



