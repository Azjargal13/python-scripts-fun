# x = (1,2)

# a, b=x
# print(a)
# print(b)

# t = ["First", "Last", "Mongolia", (2018, 02, 15)]
# f, l, c, d = t
# print(f, l, c, d)

personalRecord = ('LKim', 'Jong', '080-4745-480', '489-15-100')
f, l, *n = personalRecord

print(f, l ,n)

record = [
    ('Jeny', 10,20),
    ('Jony', 'great'),
    ('Jeny', 100,200),
    ]
def do_Jeny(x,y):
    print ("this is Jeny", x,y)

def do_Jony(s):
    print ("this is Jony", s)

for tag, *args in record:
    if tag =='Jeny':
        do_Jeny(*args)
    elif tag == 'Jony':
        do_Jony(*args)

# mapping keys to multiple values
d = {
    'a': [1,2,3,4],
    'b':[5,6,7],
    'c':[8,9,10]
}

e = {
    'a': {1,2,3,4 },
    'b':{5,6,7},
    'c':{8,9,10}
}
f = {
    'd': {1,9,8},
    'f': {5,4,3,1}
}
# print("this is common keys", d.keys() & e.keys())
# print("this is common items", e.items() & f.items())

choices = ["http", 'ftp']
url = 'http://www.google.com'

print(url.startswith(tuple(choices)))\

#concat words
parts = ['Tokyo','is','capital','city','of','Japan']

print(','.join(parts))