# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s, t):
        d1 = {}
        d2 = {}

        for character in s:
            if character not in d1:
                d1[character] = 0
            d1[character] += 1

        for character in t:
            if character not in d2:
                d2[character] = 0
            d1[character] += 1


s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
