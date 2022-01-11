#Create a function called shortcut to remove all the lowercase vowels in a given string.
def shortcut( s ):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([l for l in s if l not in vowels])