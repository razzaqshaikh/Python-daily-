#Q4: Write a function to count the number of words in a string.


def count_words(s):
    return len(s.split())


text = "Hello how are you doing today?"
print("Word count:", count_words(text))
