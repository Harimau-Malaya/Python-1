#soal 1
a = int(input("Masukkan Angka: "))
    
if (a)%2==0:
    print(a, "adalah bilangan genap.")
elif (a)%2==1:
    print(a, "adalah bilangan ganjil.")
else:
    print("Bilangan bukan bilangan genap maupun ganjil.")
  
#soal 2
b = int(input("Masukkan Angka: "))

a = 1
c = 0
while a <= b:
    c+=a
    a+=1
print("Jumlah:", c)

#soal 3
a = int(input("Masukkan Angka: "))
b = 0
c = 9

print("Tabel Perkalian", a, ":")

while b <= c:
    b += 1
    print(a, "X", b, "=", a*b)