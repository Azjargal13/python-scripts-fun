# this class serves as an abstract class or interface.

from abc import ABCMeta, abstractclassmethod

class IStream(metaclass=ABCMeta):
    @abstractclassmethod
    def read(self, maxbytes=1):
        pass
    @abstractclassmethod
    def write(self, data):
        pass
# not able to access directly, only accessible in base class
#a = IStream()

#example of encapsulation
class Employee(object):
    __salary = 0
    __name = ""
    def __init__(self):
        self.__salary = 100
        self.__name = "Semmy"
    def infoEmp(self):
        print("Employee " + self.__name + " receives " + str(self.__salary) + " Euro salary.")

e = Employee()
e.infoEmp()

from datetime import datetime

d = datetime.now()
print(d)

