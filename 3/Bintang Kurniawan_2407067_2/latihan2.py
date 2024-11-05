# Nama: Bintang Kurniawan
# NIM: 2407067
# Kelas: RPL 1 A


students = {
    "Alice" : "Computer Science",
    "Bob" : "Mathematics",
    "Charlie" : "Physics",
    "David" : "Computer Science",
    "Eva" : "Mathematics",
}

# jurusan = input("Masukkan jurusan: ").capitalize()

# print(jurusan)

# bnykSiswa = students.get(jurusan)
majors = list(students.values())

jurusan = majors.count("Computer Science")
jurusan2 = majors.count("Mathematics")
jurusan3 =  majors.count("Physics")

print("prodi Computer Science ada sebanyak", jurusan, "orang")

print("prodi Mathematics ada sebanyak", jurusan2, "orang")

print("prodi Physics ada sebanyak", jurusan3, "orang")