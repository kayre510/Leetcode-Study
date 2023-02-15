# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
    new_string = ''

    for character in s:
        if character.isalnum():
            new_string += character.lower()
    return new_string == new_string[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
