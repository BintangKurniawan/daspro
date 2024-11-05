# Bintang Kurniawan
# 2407067
# RPL 1 A

a = 0
ganjil = 0
genap = 0

while a >=0:
    number = int(input("Input bilangan : "))

    if number >= 0:
        if(number % 2 == 0 ):
            genap += number
        else:
            ganjil += number
    else:
        print(f"Jumlah bilangan genap:{genap}")
        print(f"Jumlah bilangan ganjil:{ganjil}")
        break
