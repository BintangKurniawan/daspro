# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

sum = 0

while True:
    angka = int(input("Masukkan angka: "))
    if angka < 0:
        break
    sum += angka

print(f"Jumlah: {sum}")