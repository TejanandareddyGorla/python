class demo():
    def __init__(self,a,b):
        self.__a=a #private
        self._b=b #protected
class demo2(demo):
    def output(self):
        print(self._b)
d=demo2(3,2)
d.output()



def add(a,b):
    print(a+b)
add(1,2)
add('a','b')
add([1,34],[34,76])
add((3,4),(4,6))