# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

# Program untuk mengambil list ke 2-5
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

print("List buah sebelum dilakukan perubahan", buah)

print(" ")
print("Buah pada list ke 2-5 adalah", buah[2:6])

# Program menghapus item "apel" yang kedua
buah.pop(4)

print(" ")
print("List buah setelah apel kedua dihapus",buah)

# Program mengganti nama "ceri" menjadi "cherry" 
buah[2] = "cherry"

print(" ")
print("List buah setelah ceri diubah menjadi cherry",buah)

# Program menambahkan item dengan nama "strawberry"
buah.insert(3, "strawberry")

print(" ")
print("List buah setelah ditambah strawberry",buah)

# Program mengurutkan list sesuai abjad
buah.sort()

print(" ")
print("List buah setelah diurutkan menurut abjad",buah)