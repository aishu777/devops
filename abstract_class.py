from abc import ABC,abstractmethod
class a(ABC):
    def b(self):
        pass

class c(a):
    def b(self):
        print("hiiiiiii hellooooo")
class d(a):
    def b(self):
        print("how are you")
class e(a):
    def b(self):
        print("i m fine")


q=c()
q.b()

w=d()
w.b()

r=e()
r.b()
