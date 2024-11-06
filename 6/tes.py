def penjumlahan (a,b):
    hasil = a+b
    return hasil

penjumlahan(1,2)

def pengurangan (a,b):
    print(a-b)

pengurangan(b = 2, a = 3)
pengurangan(2,3)

def greet(name = "Nigger"):
    print(f"Hello {name}")

greet()
greet("Bintang")
greet("Bintang Kurniawan")

def funcArgs(*angka):
    print(angka[:])

funcArgs(1,2,3,4,5,6,7,8,9,10)



def funcKwargs(**data):
    print(data)

def funcArgsKwargs(*angka, **data):
    print(angka)
    print(data)

funcArgsKwargs(1,2,3,4,5,6,7,8,9,10, a = 1, b = 2, c = 3)