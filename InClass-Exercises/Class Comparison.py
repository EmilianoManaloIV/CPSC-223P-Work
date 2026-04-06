class A:
    def __init__(self,/,*,a):
        self.a = a

class B(A):
    def __init__(self,/,*,a,b):
        self.b = b
        super().__init__(a=a)
class C(B):
    def __init__(self,/,*,a,b,c):
        self.c = c
        super().__init__(a=a,b=b)

superSuperSpecficClass = C(a=1,b=2,c=3)
print(superSuperSpecficClass.a, superSuperSpecficClass.b, superSuperSpecficClass.c)
