#Q2: Write a function to count the number of vowels in a string.


Name = "Shaikh RazzAque"

vowels = "aeiouAEIOU"

count = {i: Name.count(i) for i in vowels if i in Name}
print(count)
