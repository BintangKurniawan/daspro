# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

radius = int(input("Masukkan jari-jari: "))
tinggi = int(input("Masukkan tinggi: "))

def vol_tabung(r, t):
    vol = 3.14 * r * r * t

    print(f"Volume tabung adalah {vol} cm^3")

vol_tabung(radius, tinggi)