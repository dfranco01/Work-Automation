import pandas as pd
import random
from datetime import datetime, timedelta
from faker import Faker

df = pd.read_excel('log.xlsx')
faker = Faker()

#date benchmarks
today = datetime.today()
expired = today - timedelta(days=365)
ninety = today - timedelta(days=90)
sixty = today - timedelta(days=60)
thirty = today - timedelta(days=30)

def initialize():
    for i in range(len(df["PERNR NUMBER"])):
        num = ""
        for j in range(6):
            digit = str(random.randint(1, 9))
            num += digit
        df.loc[i, "PERNR NUMBER"] = float(num)
    
    for i in range(len(df)):
        df["EMPLOYEE LAST NAME"] = faker.first_name()
        df["EMPLOYEE FIRST NAME"] = faker.last_name()
        df["SUPERVISOR"] = faker.last_name()

    df["PERNR NUMBER"] = df["PERNR NUMBER"].astype(int)
    #Basic data cleaning, in real life, PERNR numbers are all unique to the individual
    #I also ensure dates are also in the correct format prior to use
    df["DATE AGREEMENT SIGNED"] = pd.to_datetime(df["DATE AGREEMENT SIGNED"], format='mixed')
    df.dropna(subset=["DATE AGREEMENT SIGNED"], inplace=True)
    df.drop_duplicates(inplace=True)

def input_check(user_input):
    acceptable = ["A", "a", "B", "b", "C", "c", "D", "d"]
    while(not user_input.isalpha() or user_input not in acceptable):
        user_input = input("Please enter a valid response: ")
    return user_input

#This function returns a dataframe subset of employees who are due for signature
def employees_due():
    benchmark = datetime.today() - timedelta(days = 365)
    df2 = df[df["DATE AGREEMENT SIGNED"] <= benchmark]
    return df2

#This function returns a dataframe subset of employees who are 90 days away from being due
def ninety_days_out():
    df2 = df[(df["DATE AGREEMENT SIGNED"] < sixty) & (df["DATE AGREEMENT SIGNED"] >= ninety)]
    return df2

#This function returns a dataframe subset of employees who are 60 days away from being due
def sixty_days_out():
    df2 = df[(df["DATE AGREEMENT SIGNED"] < thirty) & (df["DATE AGREEMENT SIGNED"] >= sixty)]
    return df2

#This function returns a dataframe subset of employees who are 30 days away from being due
def thirty_days_out():
    df2 = df[(df["DATE AGREEMENT SIGNED"] < today) & (df["DATE AGREEMENT SIGNED"] >= thirty)]
    return df2