# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

n = int(input("Masukkan jumlah deret fibonacci: "))


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

fibonacci(n)