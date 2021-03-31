import re
def invalid(cnumber):
    
def cardValid(cnumber):
    if len(cnumber)!=16:
        print('Invalid')
    elif (cnumber.isdigit() is False):
        print('Invalid')
    elif (cnumber[0])==4 or (cnumber[0])==5 or (cnumber[0])==6:
       print('Valid')
    else:
        print('Invalid')
    

cnum = 4123456789123456
cardValid(str(cnum))