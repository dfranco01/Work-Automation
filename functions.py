import pandas as pd
import random

def initialize():
    df = pd.read_excel('log.xlsx')
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
    pass

def ninety_days_out():
    pass

def sixty_days_out():
    pass

def thirty_days_out():
    pass