#declere a function tha correct list by adding comma, and at the end of list 
#declere a  function
def corrList(mylist):
    mylist[-1] = 'and ' + mylist[-1]
    mylist = ','.join(mylist)
    return mylist
#call function to print list
print(corrList(['car', 'bus', 'bike', 'truck']))
print(corrList(['apple', 'banana', 'mango', 'cherry']))