# Bintang Kurniawan
# 2407067
# RPL 1 A


username = "loginUTS"
password = "rpl2024"

print("Silakan login")

a = 3

while a > 0:
    a -=1
    user = input("Username:")
    pw = input("Password:")
    if(user == username and pw == password):
        print("Selamat datang di aplikasi Prodi RPL")
        break

    if(a == 0):
        print("Anda tidak diperkenankan mengakses aplikasi ini.")
        break
    else:
        print(f"Login Salah! Kesempatan Anda {a}x lagi.")
    
