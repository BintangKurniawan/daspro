# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A
def selisih_waktu(jam1, menit1, detik1, jam2, menit2, detik2):
        selisih_jam = jam2 - jam1
        selisih_menit = menit2 - menit1
        selisih_detik = detik2 - detik1
        
        print(f"Selisih waktu: {str(abs(selisih_jam))} jam - {str(abs(selisih_menit))} menit - {str(abs(selisih_detik))} detik")

jam1 = int(input("Masukkan jam mulai: ")) % 1000
menit1 = int(input("Masukkan menit mulai: ")) %1000
detik1 = int(input("Masukkan detik mulai: "))% 1000

jam2 = int(input("Masukkan jam selesai: ")) %1000
menit2 = int(input("Masukkan menit selesai: ")) %1000
detik2 = int(input("Masukkan detik selesai: ")) %1000

selisih_waktu(jam1, menit1, detik1, jam2, menit2, detik2)