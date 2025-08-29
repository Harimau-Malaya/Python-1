# 1. Variabel & String
var1=1
var2 = "halo"
print(f'{var1}'*100) # membuat semua variabel menjadi string dengan f-string
print(str(var1)*100) # membuat variabel menjadi string dengan str()

# 2. Operator Matematika
a= 6
b= "abcd"

print(a+len(b)) # len mengukur panjang variabel
print(1-2)
print(1/2)
print(1*2)
print(1**2)   # pangkat
print(1%2)    # sisa bagi

# 3. Percabangan IF
b = "abcdef"

if 1 != 5:
    print('a') # if tidak perlu else
else:
    print('error')

# 4. IF bersarang dengan input
b = input('masukan huruf: ')

if len(b) >= 5:
    print(b)
    if len(b) % 2 == 0:
        print(b * 3)
    elif len(b) >= 10:
        print(b * 5)
else:
    print(b * 10)

# 5. IF ELSE Nilai
n = int (input('masukan nilai: '))

if (n)>100:
    print('Nilai tidak valid')
elif (n)>=90 and (n)<=100:
    print('mantap')
else:
    print('gagal')

# 6. Array (List)
arr = ["apple", "jeruk", "kelapa", "pisang"] # array kumpulan variabel
for i in arr:
    print("saya",i)

arr = ["apple", 2, True, None, 9.90] # array bisa di isi campuran namun hanya khusus di python
for i in arr:
    print("saya",i)

# 7. Perulangan Bersarang
print("perulangan dalam perulagan")
for i in range(0,3):
    print('apel',i)
    for j in range(0,3):
        print('pisang',j)
        for h in range(0,3):
            print('jeruk',h)

# 8. FOR dengan Break
for i in range(0,10,2): # 2=beda
    print('hai',i)
    if i > 5:
        print('aple',i)
        break

# 9. FOR dengan Continue
for i in range(0,10): 
    if i == 5:
        print('aple',i)
        continue
        print('pisang')
    print('hai',i)

# 10. WHILE Loop
a= int (input('masukan angka:'))
while a <=0:
    print('a')
    break

a = True
while a:
    print('a')
    a = False

# 11. Fungsi Tambah
def tambah(a, b):
    print(a+b)

tambah(1, 4)
tambah(7, 4)
tambah(2, 6)
tambah(2, 5)
tambah(5, 4)

for i in range(0, 9):
    tambah(i,i+2)

# 12. Fungsi Kurang
def kurang (a, b):
    print(a-b)

kurang(1,10)

# 13. Pola Bintang (FOR & WHILE)
# Segitiga naik
for i in range(0,5):
    print('*'*(i+1))

# Segitiga turun
i = 6
while i > 1:
    print('*' * (i - 1))
    i -= 1

# Segitiga sama kaki
i = 0
while i < 5:
    star= '*' * (2*i + 1)
    print(star.center(9))
    i += 1

# segitiga rata kanan
for i in range(0,5):
    print(('*' * (i+1)).center(5))

