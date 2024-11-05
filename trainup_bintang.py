#Bintang Kurniawan
#2407067
#9 Zephyr
sisi_awal = ["P1", "I1", "P2", "I2", "P3", "I3"]
seberang_sungai = []
langkah_langkah = []

def pindah_ke_sisi(orang1, orang2, asal, tujuan):
    asal.remove(orang1)
    asal.remove(orang2)
    tujuan.append(orang1)
    tujuan.append(orang2)
    langkah_langkah.append(f"{orang1} dan {orang2} menyeberangi sungai")

def kembali_ke_sisi(orang, asal, tujuan):
    asal.remove(orang)
    tujuan.append(orang)
    langkah_langkah.append(f"{orang} kembali ke sisi awal")

pindah_ke_sisi("P1", "P2", sisi_awal, seberang_sungai)      
kembali_ke_sisi("P2", seberang_sungai, sisi_awal)           
pindah_ke_sisi("P3", "I3", sisi_awal, seberang_sungai)      
kembali_ke_sisi("I3", seberang_sungai, sisi_awal)           
pindah_ke_sisi("P2", "I2", sisi_awal, seberang_sungai)      
kembali_ke_sisi("I2", seberang_sungai, sisi_awal)           
pindah_ke_sisi("I1", "I2", sisi_awal, seberang_sungai)      
kembali_ke_sisi("I1", seberang_sungai, sisi_awal)           
pindah_ke_sisi("I1", "I3", sisi_awal, seberang_sungai)      

print("Langkah-langkah penyebrangan:")
for i, langkah in enumerate(langkah_langkah, 1):
    print(f"{i}. {langkah}")

print("\nPosisi akhir:")
print(f"Sisi awal: {sisi_awal}")
print(f"seberang sungai: {seberang_sungai}")
