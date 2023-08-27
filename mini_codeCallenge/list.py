#declere a function tha correct list by adding comma, and at the end of list 
#declere a  function
def corrList(mylist):
    mylist[-1] = 'and ' + mylist[-1]
    return ','.join(mylist)
    
#call function to print list
print(corrList(['car', 'bus', 'bike', 'truck']))
print(corrList(['apple', 'banana', 'mango', 'cherry']))

##---declere a function that turns list and number in to human sentance 
def listNum(myList):
    if myList[0] == 1:
        return 'there is ' + str(myList[0]) + ' ' + myList[1] + '.'
    else:
        return 'there are '+ str(myList[0]) + ' ' + myList[1] + 's.'
print(listNum(['5', 'cat']))
print(listNum(['1', 'dog']))