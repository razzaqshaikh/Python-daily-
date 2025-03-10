#Q9: Write a function to extract only the digits from a given string.


test_string = "There are 7 person in hall and 4 boys and 3"

numbers = []
for char in test_string:
    if char.isdigit():
        numbers.append(int(char))

print("The numbers list is:", numbers)

