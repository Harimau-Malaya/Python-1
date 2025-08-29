#soal 1
a= int(input('masukan angka= '))

if (a) %2==0:
    print(a, "adalah bilangan genap")
else:
    print(a, "adalah bilangan ganjil")

#soal 2
n= int(input('Masukan Angka N= '))

i=1
jumlah=0
while i <= n:
    jumlah+=i
    i+=1
print("jumlah=", jumlah) 

#soal 3
n= int (input('Masukan angka= '))
i=0
b=9

print("Tabel Perkalian", n, ":")

while i <= b:
    i+=1
    print(n, "X", i,"=",i*n)