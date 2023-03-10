# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s, t):
    flag = True
    if len(s) != len(t):
        flag = False
    else:
        letters = "abcdefghijklmnopqrstuvwxyz"
        for letter in letters:
            if s.count(letter) != t.count(letter):
                flag = False
                break
    return flag


s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
