#single inheritence
class parent():
    def output(self):
        print("i am the parent")
class child(parent):
    def outputc(self):
        print("i am the child")
c=child()
c.outputc() #child method
c.output()  #parent method


#multi-level inheritence
class Grandfather():
    def outputgf(self):
        print("i am the Granfather")
class parent(Grandfather):
    def output(self):
        print("i am the parent")
class child(parent):
    def outputc(self):
        print("i am the child")
c=child()
c.outputc() #child method
c.output() 
c.outputgf() #parent method



#multiple inheritence
class father():
    def outputgf(self):
        print("i am the father")
class mother():
    def output(self):
        print("i am the mother")
class child(father,mother):
    def outputc(self):
        print("i am the child")
c=child()
c.outputc() #child method
c.output() 
c.outputgf() #parent method

#herirical inhertence

class father():
    def outputgf(self):
        print("i am the father")
class child1(father):
    def output(self):
        print("i am the child1")
class child2(father):
    def outputc(self):
        print("i am the child2")
c=child1()
c2=child2()
c.output() 
c.outputgf() #parent method
c2.outputc()
c2.outputgf()


