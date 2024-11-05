# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

nama = input("Masukkan nama: ").title()
jk = input("Masukkan jenis kelamin: ").title()
umur = int(input("Masukkan umur: "))
tinggi_badan = int(input("Masukkan tinggi badan: "))
iq = int(input("Masukkan iq: "))

if umur >=18 and umur <= 25:
    if iq >= 130:
        if jk == "Pria" or jk == "Laki-Laki" or jk == "Laki Laki" :
            if tinggi_badan >= 175:
                print(f"{nama} dapat menjadi model catwalk")
            else:
                print(f"{nama} tidak dapat menjadi model catwalk karena tinggi badan kurang dari 175 cm")
        elif jk == "Wanita" or jk == "Perempuan":
            if tinggi_badan >= 170:
                print(f"{nama} dapat menjadi model catwalk")
            else:
                print(f"{nama} tidak dapat menjadi model catwalk karena tinggi badan kurang dari 170 cm")
        else:
            print(f"{nama} dapat menjadi model catwalk karena jenis kelamin hanya ada dua.")
    else:
        print(f"{nama} tidak dapat menjadi model catwalk karena IQ kurang dari 130")
else:
    print(f"{nama} dapat menjadi model catwalk karena umur kurang dari 18 atau lebih dari 25")

