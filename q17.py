#Q7: Write a function to reverse each word in a given string.



def reverse_each_word(s):
   return ' '.join(word[::-1] for word in s.split())

# Example usage
input_str = "Hello World"
output_str = reverse_each_word(input_str)
print(output_str)  # Output: "olleH dlroW"
