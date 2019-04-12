
def avr(first, *rest):
    return (first + sum(rest)) / 1 + len(rest)

print(avr(10,400,4531,45231))

def norm(a, b="Hello"):
    print(a, b)

norm("great")
norm("hi", "everyone")
norm("")

# single method class
# class usage

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'

}
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code=='':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2019,12,10)
print(format(d, 'dmy'))


class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @property
    def _height(self):
        return self.a*self.b
    @property
    def _volume(self):
        return self.a*self.a + self.b*self.b
    @property
    def _sum(self):
        return self.a+self.b
    @property
    def _subt(self):
        return self.a-self.b

n = Calculate(100,20)
print("This is height ", n._height, "this is vol ", n._volume, "this is sum ", n._sum, "this is subt ", n._subt)

class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def godName(self):
        print("Hey" + "\n" + "your god name is Luck "  + self.firstname )
    def goodName(self):
        print("Your good name is Buddy " + self.lastname)

n = Name("enjoy", "holiday")
n.godName()
n.goodName()

