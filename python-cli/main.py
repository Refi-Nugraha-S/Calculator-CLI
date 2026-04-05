from function import addition, subtraction, multiplication, division
from text import text

text()

while True:

    start = input("START or QUIT (y/n) = ")

    if start == "n":
        print("Byee !")
        break

    elif start == "y":

        print("\n")

        try:

            number1 = float(input("Enter the number A = "))
            number2 = float(input("Enter the number B = "))
            operation = int(input("Choose operator (+ / - / x / :) 1/2/3/4 = "))

            if operation in ["quit", "exit", "q"]:
                print("Thankss for use this !, Byee")
                break

            elif operation == 1:
                print("Result =", (addition(number1, number2)), "\n")
            elif operation == 2:
                print("Result =", (subtraction(number1, number2)), "\n")
            elif operation == 3:
                print("Result =", (multiplication(number1, number2)), "\n")
            elif operation == 4:
                print("Result =", (division(number1, number2)), "\n")

        # ERROR
        except ValueError:
            print("Error: Enter a valid number ! \n")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero ! \n")
        except Exception as e:
            print("Something wrong: {e}")
            print("Send me a message about this error \n")
        except KeyboardInterrupt:
            print("\n")
            print("Error: Cancel by user ! \n")
            break
