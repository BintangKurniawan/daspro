# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

passw = "Latihan"
chance = 3

def login(pw, chance):
    if pw == passw:
        print("Selamat datang")
    elif (chance > 0):
        print(f"Password salah, Anda hanya punya {chance}x kesempatan lagi.")
    else:
        print("Anda tidak diperkenankan mengakses aplikasi ini.")

while True:
    chance -= 1
    username = input("Username: ")
    pw = input("Password: ")

    if chance == 0:
        login(pw, chance)
        break

    if pw != passw:
        login(pw, chance)
    else:
        chance +=1
        login(pw, chance)