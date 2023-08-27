#decclere a function that use a condition of true or false on string's list
def myfunc(string): 
   if string[0] == 'a':
       return 'adverk'
   else:
       return 'zebra'
   
print(myfunc('tomato'))
print(myfunc('apple'))
            

# declere a function to slice a string
def slicing(string):
    return string[::-1]

print(slicing('shakuntala'))
print(slicing('HI!'))


def gerund(string):
    if string[-3:] == 'ing':
        return 'to ' + string[:-3]
    else:
        return 'thats not a gerund'
    
print(gerund('going'))
print(gerund('eating'))
print(gerund('builded'))
    