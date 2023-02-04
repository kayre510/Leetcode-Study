# Given an array of integers, where all elements but one occur twice, find the unique element.
# a = [1,2,3,4,3,2,1]

#return the element that occurs only once

def lonelyinteger(a):
    count = [] # create an empty array to store the numbers
    for number in a: #iterate through the a array
        if number in count: # if the number is in count
            count.remove(number) # remove it
        else: #else
            count.append(number) #add the number to the count
    return count[0] #return the number at the zero index
