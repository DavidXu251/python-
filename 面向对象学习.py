
class A:
    def __init__(self):
        self.a=1

class B:
    def __init__(self):
        b=2

class C(A,B):
    def __init__(self):
        super().__init__()
        print(self.a)


C()
