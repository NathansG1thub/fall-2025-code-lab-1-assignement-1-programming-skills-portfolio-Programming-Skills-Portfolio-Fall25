## Assessment 1 Portfolio

# Nathanael Van B. Zamora
# Level 4 Pathway Student
# Student ID: 01 - 25 -345

## Exercise 1: Coding is Cool
word1 = "Coding"
word2 = "is"
word3 = "cool"
# Use string concatenation to combine the variables and print the phrase
print(f"{word1} {word2} {word3}")

## Exercise 2: Simple Sums 
apple = 8
banana = 10
total_fruits = apple + banana
print(f"there are a total of {total_fruits} fruits")

## Exercise 3: Bibliography
dict = {}
dict["Name"] = "Nathanael Van B. Zamora"
dict["Hometown"] = "Manila, Philippines"
dict["Age"] = "18"

for key in dict:
    print(key, ":", dict[key])

## Exercise 4: Primitive Quiz
answer = input("What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct! Paris is the capital of France.")
else:
    print("Wrong! The capital of France is Paris.")

## Exercise 5: Days of the Month
days_in_month = {
    1: 31,   # January
    2: 28,   # February (non-leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

month_number = int(input("Enter the month number (1-12): "))

if month_number in days_in_month:
    print(f"There are {days_in_month[month_number]} days in month {month_number}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")  

## Exercise 6: Brute Force Attack
correct_password = "12345"

while True:
    password = input("Enter Nathan's password: ")
    if password == correct_password:
        print("Correct password entered! Access granted.")
        break
    else:
        print("Incorrect password. Try again.")

## Exercise 7: Some Counting
print("1. Count up from 0 to 50 in increments of 1:")
for i in range(0, 51):
    print(i, end=" ")
print("\n")

print("2. Count down from 50 to 0 in decrements of 1:")
for i in range(50, -1, -1):
    print(i, end=" ")
print("\n")

print("3. Count up from 30 to 50 in increments of 1:")
for i in range(30, 51):
    print(i, end=" ")
print("\n")

print("4. Count down from 50 to 10 in decrements of 2:")
for i in range(50, 9, -2):
    print(i, end=" ")
print("\n")

print("5. Count up from 100 to 200 in increments of 5:")
for i in range(100, 201, 5):
    print(i, end=" ")
print("\n")

## Exercise 8: Simple Search
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = "Sam"

if search_name in names:
    index = names.index(search_name)
    print(f"{search_name} is found in the list at position {index}!")
else:
    print(f"{search_name} is not in the list.")

## Exercise 9: Hello
def hello():
    print("Hello")  

def main():
    hello()  

if __name__ == "__main__":
    main()

## Exercise 10: Is it even
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