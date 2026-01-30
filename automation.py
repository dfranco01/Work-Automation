import functions

def main():
    functions.initialize()
    print("You may see who is due for an agreement signature, as well as who will be due in 90, 60, and 30 days respectively.")
    print("What would you like to view?")
    choice = input("Choices are as follows: a = expired, b = due in 30 days, c = due in 60 days, d = due in 90 days. All other input is invalid: ")
    choice = functions.input_check(choice)
    while(True):
        match choice.upper():
            case "A":
                functions.employees_due()
                continue_working = input("Continue working? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break
            case "B":
                functions.thirty_days_out()
                continue_working = input("Continue working? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break
            case "C":
                functions.sixty_days_out()
                continue_working = input("Continue working? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break
            case "D":
                functions.ninety_days_out()
                continue_working = input("Continue working? Enter a for yes, any other input will exit the program: ")
                if continue_working.upper() == "A":
                    continue
                break

    

if __name__ == "__main__":
    main()