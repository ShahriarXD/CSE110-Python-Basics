#PROBLEM 5  (10 points possible)
#Suppose you are given two strings (they may be empty), s1 and s2. You
#would like to "lace" these strings together, by successively alternating
#elements of each string (starting with the first character of s1). If
#one string is longer than the other, then the remaining elements of the
#longer string should simply be added at the end of the new string.

#For example, if we lace 'abcd' and 'efghi',
#we would get the new string: 'aebfcgdhi'.

#Write an iterative procedure, called laceStrings(s1, s2) that does this.

#Note: You will only get ten checks. Use these judiciously.

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
print laceStrings('abcdef', 'ghi'), " Should be agbhcidef."
