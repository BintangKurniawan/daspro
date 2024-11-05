# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

# Program untuk mengambil tuple ke 2-5
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

print("Tuple buah sebelum dilakukan perubahan", buah)

print(" ")
print("Buah pada tuple ke 2-5 adalah",buah[2:6])

# Program menghapus item "durian" dihapus
x = list(buah)

x.pop(3)

buah = tuple(x)

print(" ")
print("Tuple buah setelah durian dihapus",buah)

# Program menambah item "manggis" diantara item "jeruk" dan "ceri"
x = list(buah)

x.insert(2, "manggis")

buah = tuple(x)

print(" ")
print("List buah setelah ditambah manggis diantara jeruk dan ceri",buah)