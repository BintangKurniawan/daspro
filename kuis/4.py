# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

daftarBarang = ["Kerudung", "Kemeja", "Rok", "Celana Panjang", "Baju Renang","Topi", "Tas", "Sepatu", "Kacamata"]

print(f"Daftar barang jualan pada bulan Juli:\n {daftarBarang}\n jumlahnya: {daftarBarang.__len__()}")

daftarBarang[4] = "Piyama"
daftarBarang.append("Ikat Rambut")
daftarBarang.append("Sendal")

print()

print(f"Daftar barang jualan pada bulan ini:\n {daftarBarang}\n jumlahnya: {daftarBarang.__len__()}")