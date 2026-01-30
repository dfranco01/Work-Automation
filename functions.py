import pandas as pd
import random
from datetime import datetime, timedelta

df = pd.read_excel('log.xlsx')

def initialize():
    for i in range(len(df["PERNR NUMBER"])):
        num = ""
        for j in range(6):
            digit = str(random.randint(1, 9))
            num += digit
        df.loc[i, "PERNR NUMBER"] = float(num)
    df["PERNR NUMBER"] = df["PERNR NUMBER"].astype(int)

def input_check(user_input):
    while(not user_input.isalpha()):
        user_input = input("Please enter a valid response: ")
    return user_input

def employees_due():
    today = datetime.today()
    benchmark = timedelta(days = 365)
    due = df.loc[["DATE AGREEMENT SIGNED" <= (today - benchmark) ]]
    return due

def ninety_days_out():
    today = datetime.today()
    benchmark = timedelta(days = 365)
    due = df.loc[["DATE AGREEMENT SIGNED" <= (today - benchmark) ]]
    return due

def sixty_days_out():
    today = datetime.today()
    benchmark = timedelta(days = 365)
    due = df.loc[["DATE AGREEMENT SIGNED" <= (today - benchmark) ]]
    return due

def thirty_days_out():
    today = datetime.today()
    benchmark = timedelta(days = 365)
    due = df.loc[["DATE AGREEMENT SIGNED" <= (today - benchmark) ]]
    return due