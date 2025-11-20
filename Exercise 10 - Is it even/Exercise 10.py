## Exercise 10: Is it even

# Nathanael Van B. Zamora
# Date: November 17th, 2025
# Level 4 Pathway Student
# Student ID: 01 - 25 -345

def _takeinput(msg):
    while True:
        user_input = input(msg)
        try:
            return int(user_input)  
        except ValueError:
            try:
                return float(user_input)  
            except ValueError:
                print("Invalid input. Please enter a number.")

def odd_or_even(x):
     if x % 2 == 0:
        return "Even"
     else:
        return "Odd"

while True:
    x = _takeinput("Enter a number: ")
    print(f"{x} is an {odd_or_even(x)} number.")
    while True:
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont == 'y':
            break  
        elif cont == 'n':
            print("Goodbye!")
            exit()  
        else:
            print("Please enter 'y' or 'n'.")
