# Bintang Kurniawan
# 2407067
# RPL 1 A
a = 3

prev_num = {"num": 1}

bigger_num = 0

number = int(input("Input bilangan : "))
prev_num["num"] = number

while a >= 0:
    a-=1
    if(a == 0):
        break
    cur_num = int(input("Input bilangan : "))

    if(cur_num > prev_num["num"]):
        bigger_num += cur_num
        a +=2
    
    prev_num["num"] = cur_num
    # print(prev_num["num"])
    # print(a)

print(f"Hasil penjumlahan nilai yang membesar adalah {bigger_num}")
    


