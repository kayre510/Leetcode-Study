def longestPalindrome(s):
        frequency_dictionary = {}
        for character in s:
            if character in frequency_dictionary:
                frequency_dictionary[character] += 1
            else:
                frequency_dictionary[character] = 1

        length = 0
        odd_numbers = 0
        for character in frequency_dictionary:
            length += frequency_dictionary[character] // 2 * 2

        for character in frequency_dictionary:
            if frequency_dictionary[character] % 2 == 1:
                odd_numbers += 1
        if odd_numbers > 0:
            length += 1
        return length

s = "abccccdd"

print(longestPalindrome(s))
#hey11111ttttttttfff
##########
