##-------Given two strings s and t, return true if t is an anagram of s, 
# and false otherwise.An Anagram is a word or phrase formed by rearranging the 
# letters of a different word or phrase, typically using all the original letters 
# exactly once.-------

# def isAnagram(a,b):
#     countA = {}
#     countB = {}
#     if len(a) != len(b):
#         return False
#     for i in range(len(a)):
#         countA[a[i]] = 1 + countA.get(a[i],0)
#         countB[b[i]] = 1 + countB.get(b[i], 0)
#     return countA == countB


# s = input('Enter character for s: ')
# t = input('Enter character for t: ')

# print(isAnagram(s, t))


def angram(x, y):
    if len(x) != len(y):
        return False
    countX = {}
    countY = {}
    for i in range(len(x)):
        countX[x[i]] = 1 + countX.get(x[i], 0)
        countY[y[i]] = 1 + countY.get(y[i], 0)
    return countX == countY

s = input('Enter character for s: ')
t = input('Enter character for t: ')
print(angram(s, t))