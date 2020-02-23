class test(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
        def __call__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c


instance1 = test( 1, 2, 3)

print(instance1.a) #prints 1
print(instance1.b) #prints 2
print(instance1.c) #prints 3

"""
Technically __init__ is called once by __new__ when object is created, so that it can be initialized.

With __call__ you can redefine the same object as if it were new.

"""