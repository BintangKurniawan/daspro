# Bintang Kurniawan
# 2407067
# RPL 1 A

nim = int(input("Input 3 digit NIM terakhir : "))

nim = (nim % 1000)
# print(nim)

if (nim >= 151):
    if(nim % 2 ==0):
        print("Silakan masuk ke kelas K8")
    else:
        print("Silakan masuk ke kelas K7")
elif (nim >= 101 and nim <= 150):
    if(nim % 2 == 0 ):
        print("Silakan masuk ke kelas K6")
    else:
        print("Silakan masuk ke kelas K5")
elif (nim >= 51 and nim <= 100):
    if(nim % 2 == 0):
        print("Silakan masuk ke kelas K4")
    else:
        print("Silakan masuk ke kelas K3")
else:
    if(nim % 2 == 0):
        print("Silakan masuk ke kelas K2")
    else:
        print("Silakan masuk ke kelas K1")