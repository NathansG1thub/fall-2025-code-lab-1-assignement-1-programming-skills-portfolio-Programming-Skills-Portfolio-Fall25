## Exercise 6: Brute Force Attack

# Nathanael Van B. Zamora
# Date: November 10th, 2025
# Level 4 Pathway Student
# Student ID: 01 - 25 -345

correct_password = "12345"

while True:
    password = input("Enter Nathan's password: ")
    if password == correct_password:
        print("Correct password entered! Access granted.")
        break
    else:
        print("Incorrect password. Try again.")