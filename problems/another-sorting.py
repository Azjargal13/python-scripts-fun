#def sortsmart(s):
import string
def sortFun(string):
    #print(*sorted(string, key=lambda s: (s.lower(), s.upper(), s.isdigit() and int(s)%2==0,)))
    print(*sorted(string, key=(string.ascii_letters + '1357902468').index, sep='')
inpu = 'SQERorting123445432023'
#print(*(sorted(inpu, key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')
sortFun(inpu)