# import pandas as pd

# data = {
#     "nama": ["bintang", "kurniawan"],
#     "umur": [20, 20],
#     "pekerjaan": ["mahasiswa", "mahasiswa"]
# }
# df = pd.DataFrame(data)
# print(df)


# Fungsi untuk mendapatkan ID terakhir dari file
def get_last_id(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if lines:  # Jika file tidak kosong
                last_line = lines[-1]  # Ambil baris terakhir
                last_id = int(last_line.split(',')[0])  # Ambil ID dari baris terakhir
                return last_id
            else:
                return 0  # Jika file kosong, mulai dari ID 0
    except FileNotFoundError:
        return 0  # Jika file belum ada, mulai dari ID 0

# File tempat menyimpan data
filename = 'text.txt'

# Dapatkan ID terakhir dan hitung ID baru
last_id = get_last_id(filename)
new_id = last_id + 1

# Ambil input dari pengguna
nama_baru = input("Masukkan Nama: ")
kota_baru = input("Masukkan Kota: ")
telepon_baru = input("Masukkan No. Telepon: ")

# Gabungkan data dengan format dipisahkan koma
data_baru = f"{new_id},{nama_baru},{kota_baru},{telepon_baru}\n"

# Menambahkan data baru ke dalam file
with open(filename, 'a') as file:
    file.write(data_baru)

print(f"Data berhasil ditambahkan dengan ID: {new_id}")
