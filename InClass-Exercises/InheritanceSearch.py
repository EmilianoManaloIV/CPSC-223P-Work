class A:
    def rk(self):
        print("IN class A")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
r = D()
r.rk()