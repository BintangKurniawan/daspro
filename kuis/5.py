# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A
import os

mobil = {
    "Merk": "Honda",
    "Tipe": "HRV",
    "Tahun": 2018,
    "Warna" : "Hitam",
    "No. Polisi": "D 1234 ABC",
    "Bensin": "Pertalite",
    "Tranmisi": "Manual"
}
 
print(f"Mobil lama Pak Oki adalah:\nMerk: {mobil["Merk"]}\nTipe mobil: {mobil["Tipe"]}\nTahun keluaran: {mobil["Tahun"]}\nWarna: {mobil["Warna"]}\nNo. Polisi: {mobil["No. Polisi"]}\nBensin: {mobil["Bensin"]}\nTransmisi: {mobil["Tranmisi"]}")

print()

print("Masukkan informasi detail mobil baru")
mobil["Merk"] = input("Merk:")
os.system("cls")
mobil["Tipe"] = input("Tipe mobil:")
os.system("cls")
mobil["Tahun"] = input("Tahun Keluaran:")
os.system("cls")
mobil["Warna"] = input("Warna:")
os.system("cls")
mobil["No. Polisi"] = input("No. Polisi:")
os.system("cls")
mobil["Bensin"] = input("Bensin:")
os.system("cls")
mobil["Tranmisi"] = input("Transmisi:")
os.system("cls")
print()
os.system("cls")
print("-----------***-----------")
print(f"Mobil baru Pak Oki adalah:\nMerk: {mobil["Merk"]}\nTipe mobil: {mobil["Tipe"]}\nTahun keluaran: {mobil["Tahun"]}\nWarna: {mobil["Warna"]}\nNo. Polisi: {mobil["No. Polisi"]}\nBensin: {mobil["Bensin"]}\nTransmisi: {mobil["Tranmisi"]}")
print("-----------***-----------")