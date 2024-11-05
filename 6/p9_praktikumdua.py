# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

def nilaiTotal(*nilai):
    print(f"Input: {nilai}")
    print(f"Total:{nilai} = {sum(nilai)}")
    print(f"Rata-rata: {sum(nilai) / len(nilai)}")

total = []
while True:
    inputNilai = int(input("Masukkan Nilai: "))
    if inputNilai == "":
        break
    else:
        nilai = int(inputNilai)
        total.append(nilai)


nilaiTotal(*total)