from InquirerPy import prompt
import os

def cek_pendataan():
    lanjut = True

    opt = [
        {
            "type": "list",  # Menggunakan list prompt
            "name": "Option",  # Nama dari key yang digunakan di jawaban
            "message": "Pilih salah satu opsi:",  # Pesan yang ditampilkan ke pengguna
            "choices": ["1. Tambah transaksi", "2. Cek data hari ini", "3. Cek pendataan yang lalu", "4. Kembali ke menu utama"]  # Pilihan opsi
        }
    ]
    while lanjut == True:
        os.system('cls')
        print("========Option========")
        answer = prompt(opt)
        if answer["Option"] == "1. Tambah transaksi":
            print("TAMBAH TRANSAKSI")
        elif answer["Option"] == "2. Cek data hari ini":
            print("CEK DATA HARI INI")
        elif answer["Option"] == "3. Cek pendataan yang lalu":
            print("CEK PENDATAAN YANG LALU")
        elif answer["Option"] == "4. Kembali ke menu utama":
            print("KEMBALI KE MENU UTAMA")
            lanjut = False
            

def main():
    opt = [
        {
            "type": "list",  # Menggunakan list prompt
            "name": "Option",  # Nama dari key yang digunakan di jawaban
            "message": "Pilih salah satu opsi:",  # Pesan yang ditampilkan ke pengguna
            "choices": ["1. Cek pendataan", "2. Cek produk", "3. Cek pengutang", "4. Exit"]  # Pilihan opsi
        }
    ]
    lanjut = True
    print("========WElcome To Loop========")
    while lanjut == True:
        os.system('cls')
        print("========Option========")
        answer = prompt(opt)
        if answer["Option"] == "1. Cek pendataan":
            cek_pendataan()
        elif answer["Option"] == "2. Cek produk":
            print("Cek produk")
        elif answer["Option"] == "3. Cek pengutang":
            print("Cek pengutang")
        elif answer["Option"] == "4. Exit":
            print("Exit")
            lanjut = False




if __name__ == "__main__":
    main()