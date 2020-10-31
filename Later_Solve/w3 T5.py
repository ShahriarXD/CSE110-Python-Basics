
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    newString = ''
    lenS1 = len(s1)
    lenS2 = len(s2)
    if lenS1 == lenS2:
      for i in range(lenS1):
        newString += s1[i] + s2[i]
    else:
      lenToDo = min(lenS1, lenS2)
      for i in range(lenToDo):
        newString += s1[i] + s2[i]
      if lenS1 > lenS2:
        newString += s1[lenS2:]
      else:
        newString += s2[lenS1:]
    return newString

    
#Test cases:
print laceStrings('abcd', 'efgh'), ' Should be aebfcgdh.'
print laceStrings('abcd', 'efghi'), ' Should be aebfcgdhi.'
