# Bintang Kurniawan
# 2407067
# RPL 1 A

number = int(input("Masukkan nilai N = "))

prime = 0

for i in range (number):
    num = int(input(f"Masukkan bilangan ke-{i+1} = "))
    if (num == 2):
        prime += num
    

    
    if((num % 3 != 0 and num % 2 != 0 and num % 5 != 0 and num % 7 != 0) and num % num == 0):
        prime += num

print(f"Jumlah bilangan prima adalah = {prime}")
