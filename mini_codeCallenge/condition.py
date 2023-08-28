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

##declere a function to  to remove ing from strng and add to befor string
def gerund(string):
    if string[-3:] == 'ing':
        return 'to ' + string[:-3]
    else:
        return 'thats not a gerund'
    
print(gerund('going'))
print(gerund('eating'))
print(gerund('builded'))


##declere a function that return values for keys in dictionary
mydic = {'CA': 'california', 'NY': 'New York', 'WA': 'Washington', 'FL': 'florida'}
def myfunc(string):
    return mydic[string]

print(myfunc('CA'))
print(myfunc('NY'))


##declere function masge turn to morse code 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def conMorse(string):
    newstring = ''
    for letters in string:
        newstring += MORSE_CODE_DICT[letters]
    return newstring

print(conMorse('LONDON1'))