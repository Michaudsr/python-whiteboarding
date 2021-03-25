#Brute force method of solving if a string has all unique characters.
def is_unique(s):
    pass

# defining the first for loop
# there will be  nested for loops to solve
# We will loop through every character in the string until the second to last
# We'll be comparing each character to the ones following it, and since there are none after the last character we stop at the second to last.
def is_unique(s):
  for i in range(len(s) - 1):

# We will now make a for loop inside the first for loop
# This loop will start with the next spot in the list which we'll call j
# Index j will traverse the list until the end, comparing it to the character at the first index, i.
# We'll return False if they match, meaning the characters in the string are not unique.
def is_unique(s):
  for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
      if s[j] == s[i]:
        return False

# The Last step is to return True if the nested for loop successfully compares each character in the list and does not find a match, meaning that each character is unique
def is_unique(s):
  for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
      if s[j] == s[i]:
        return False
  return True

