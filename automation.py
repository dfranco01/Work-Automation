import functions
from IPython.display import display

#user workflow
def main():
    functions.initialize()
    print("You may see who is due for an agreement signature, as well as who will be due in 90, 60, and 30 days respectively.")
    while(True):
        #the user can now choose what subset of data they are interested in viewing
        #as well as return to view another subset
        print("What would you like to view?")
        #choice = input("Choices are as follows: a = expired, b = due in 30 days, c = due in 60 days, d = due in 90 days. All other input is invalid: ")
        choice = functions.input_check(input("Choices are as follows: a = expired, b = due in 30 days, c = due in 60 days, d = due in 90 days. All other input is invalid: "))
        match choice.upper():
            case "A":
                df = functions.employees_due()
                display(df)
                export = input("Export table into Excel file? Enter a for yes, any other key will imply no: ")
                if export.upper() == "A":
                    print("Exported! Note: you'll have to expand the columns to see the data properly")
                    df.to_excel("Expired.xlsx")
                continue_working = input("View other tables? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break
            case "B":
                df = functions.thirty_days_out()
                display(df)
                export = input("Export table into Excel file? Enter a for yes, any other key will imply no: ")
                if export.upper() == "A":
                    print("Exported! Note: you'll have to expand the columns to see the data properly")
                    df.to_excel("thirty.xlsx")
                continue_working = input("View other tables? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break
            case "C":
                df = functions.sixty_days_out()
                display(df)
                export = input("Export table into Excel file? Enter a for yes, any other key will imply no: ")
                if export.upper() == "A":
                    print("Exported! Note: you'll have to expand the columns to see the data properly")
                    df.to_excel("sixty.xlsx")
                continue_working = input("View other tables? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break
            case "D":
                df = functions.ninety_days_out()
                display(df)
                export = input("Export table into Excel file? Enter a for yes, any other key will imply no: ")
                if export.upper() == "A":
                    print("Exported! Note: you'll have to expand the columns to see the data properly")
                    df.to_excel("ninety.xlsx")
                continue_working = input("View other tables? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break
    print("Thank you for using!")

    

if __name__ == "__main__":
    main()