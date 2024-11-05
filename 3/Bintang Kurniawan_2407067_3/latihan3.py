# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"},
}

namaStudent = input("Inputkan nama siswa: ").title()

info = student_info.get(namaStudent, {})

print(f"Umur {namaStudent} adalah { info.get('age', 'unknown')} dan Prodinya adalah { info.get('major', 'unknown')}")
