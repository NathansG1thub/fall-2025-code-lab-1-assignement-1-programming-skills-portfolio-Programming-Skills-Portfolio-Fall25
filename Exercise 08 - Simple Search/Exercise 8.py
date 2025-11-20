## Exercise 8: Simple Search

# Nathanael Van B. Zamora
# Date: November 15th, 2025
# Level 4 Pathway Student
# Student ID: 01 - 25 -345

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = "Sam"

if search_name in names:
    index = names.index(search_name)
    print(f"{search_name} is found in the list at position {index}!")
else:
    print(f"{search_name} is not in the list.")