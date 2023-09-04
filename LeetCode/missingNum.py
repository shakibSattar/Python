##-----Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.-----

def missingArray(num):
    for n in range(len(num)+1):
        if n not in num:
            return n
        
num = [0,1,2,3,5,6]
print(missingArray(num))


##--Follow up: Could you implement a solution using only O(1) extra space complexity
# and O(n) runtime complexity?-----
def MissingArray(num):
    x1 = 0
    x2 = 0
    for i in range(len(num)+1):
        x1 = x1^ i
    for i in range (len(num)): 
        x2 = x2^num[i]  
    return x1^x2

num = [0,1,2,3,5,6,7,8,9]
print(MissingArray(num))

