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
    #Basic data cleaning, in real life, PERNR numbers are all unique to the individual
    df["DATE AGREEMENT SIGNED"] = pd.to_datetime(df["DATE AGREEMENT SIGNED"], format='mixed')
    df.dropna(subset=["DATE AGREEMENT SIGNED"], inplace=True)
    df.drop_duplicates(inplace=True)

def input_check(user_input):
    while(not user_input.isalpha()):
        user_input = input("Please enter a valid response: ")
    return user_input

#This function returns a dataframe subset of employees who are due for signature
def employees_due():
    benchmark = datetime.today() - timedelta(days = 365)
    df2 = df[df["DATE AGREEMENT SIGNED"] < benchmark]
    return df2

#This function returns a dataframe subset of employees who are 90 days away from being due
def ninety_days_out():
    today = datetime.today()
    upper_bound = today
    lower_bound = today - timedelta(days = 90)
    df2 = df[(df["DATE AGREEMENT SIGNED"] < upper_bound) & (df["DATE AGREEMENT SIGNED"] > lower_bound)]
    return df2

#This function returns a dataframe subset of employees who are 60 days away from being due
def sixty_days_out():
    today = datetime.today()
    upper_bound = today
    lower_bound = today - timedelta(days = 60)
    df2 = df[(df["DATE AGREEMENT SIGNED"] < upper_bound) & (df["DATE AGREEMENT SIGNED"] > lower_bound)]
    return df2

#This function returns a dataframe subset of employees who are 30 days away from being due
def thirty_days_out():
    today = datetime.today()
    upper_bound = today
    lower_bound = today - timedelta(days = 30)
    df2 = df[(df["DATE AGREEMENT SIGNED"] < upper_bound) & (df["DATE AGREEMENT SIGNED"] > lower_bound)]
    return df2