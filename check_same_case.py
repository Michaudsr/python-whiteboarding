#Write a function that will check if two given characters are the same case.

#'a' and 'g' returns 1

#'A' and 'C' returns 1

#'b' and 'G' returns 0

#'B' and 'g' returns 0

#'0' and '?' returns -1

#If any of characters is not a letter, return -1.

#If both characters are the same case, return 1.

#If both characters are letters and not the same case, return 0.

def same_case(a, b): 
    if a.isalnum() and b.isalnum() and a.isupper() == b.isupper():
        return 1
    elif a.isalnum() and b.isalnum() and a.isupper() != b.isupper():
        return 0
    else:
        return -1
#print(same_case("a", "a"))
