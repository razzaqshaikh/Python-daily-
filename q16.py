#Q6: Write a function to remove duplicate characters from a string.


s = "Classes"

seen = set() 
res = ""     

for char in s:
    if char not in seen:
        seen.add(char)
        res += char
print(res)
