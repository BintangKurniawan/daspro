import os

# os.system("cls")
def edit_data_by_id(filename, edit_id, new_name, new_city, new_phone):
    try:
        # Baca seluruh isi file
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Flag untuk mengecek apakah ID ditemukan
        id_found = False
        
        # List untuk menyimpan data yang telah diedit
        new_lines = []
        
        # Loop melalui setiap baris dan cek apakah ID cocok
        for line in lines:
            data = line.strip().split(',')
            current_id = int(data[0])
            
            if current_id == edit_id:
                # Jika ID ditemukan, edit data
                new_line = f"{edit_id},{new_name},{new_city},{new_phone}\n"
                new_lines.append(new_line)
                id_found = True
            else:
                # Jika ID tidak cocok, simpan baris lama
                new_lines.append(line)
        
        if not id_found:
            print(f"Data dengan ID {edit_id} tidak ditemukan.")
            return
        
        # Tulis ulang file dengan data yang telah diperbarui
        with open(filename, 'w') as file:
            file.writelines(new_lines)
        
        print(f"Data dengan ID {edit_id} berhasil diperbarui.")
    
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")

# Contoh penggunaan fungsi
filename = 'text.txt'
edit_id = int(input("Masukkan ID yang ingin diedit: "))
new_name = input("Masukkan Nama baru: ")
new_city = input("Masukkan Kota baru: ")
new_phone = input("Masukkan No. Telepon baru: ")

# Panggil fungsi untuk mengedit data
edit_data_by_id(filename, edit_id, new_name, new_city, new_phone)