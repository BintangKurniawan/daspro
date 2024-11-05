# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

nilai = int(input("Masukkan Nilai: "))

if nilai > 0:
    print("Nilai positif")
    if nilai % 2 == 0:
        print("Juga Nilai Genap")
    else:
        print("Juga Nilai Ganjil")
elif nilai < 0:
    print("Nilai negatif")
    if nilai % 2 == 0:
        print("Juga Nilai Genap")
    else:
        print("Juga Nilai Ganjil")
else:
    print("Nol")