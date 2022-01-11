#You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all ASCII characters.

def uni_total(s):
    if(len(s) == 0):
        return 0
    else :
        return sum([ord(i) for i in s])