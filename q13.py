#Q3: Write a function to check if a string is a palindrome (same forward and backward).


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
