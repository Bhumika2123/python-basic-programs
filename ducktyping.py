class A:
    def talk(self):
        print("a is talking")

class B:
    def talk(self):
        print("b is talking")

class C:
    def catch(self, duck):
        duck.talk()
        print("this is c")

a= A()
b=B()
c=C()
c.catch(a)
