for i in range(3):
    for j in range(3):
        print(f"({i},{j})")

for i in "Jawa":
    print(i)

jawa = ["Bali", "Jawa", "Sulawesi", "Nusa Tenggara"]

for i in jawa:
    print(i)

print()
for i in range(len(jawa)):
    print(jawa[i])

angka = 0
while ( angka < 8):
    print(angka)
    angka += 1.999999999999


print()
angka1 = [1,2,3,4,5]

for i in angka1:
    print(i)
    if i == 3:
        break

print()

for i in angka1:
    if i == 3:
        break
    print(i)


print()

for i in angka1:
    if i == 3:
        continue
    print(i)

print()


print("*" * 20)

angka2 = [1,2,]
angka3 = [1,2,3,4]

for i in angka1:
    for j in angka2:
        for k in angka3:
            print(i,j,k)


for i in range(100,0, -22):
    print(i)

for i in range (1, 6):
    print(i)