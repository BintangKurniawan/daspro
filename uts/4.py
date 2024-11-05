# Bintang Kurniawan
# 2407067
# RPL 1 A

n = int(input("Masukkan berapa kali ="))
print()

for i in range(n, 0, -1):
    print(f"{i} bebek kecil berenang")
    print("Menyusuri sungai yang deras")
    print("Induknya mencari kwek kwek kwek")
    if(i-1 > 0):
        print(f"Hanya {i-1} ekor yang pulang")
        print()
    else:
        print("Dan semua bebek kecil pulang, aha!")