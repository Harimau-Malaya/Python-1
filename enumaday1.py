var1=1
var2 = "halo"
print(f'{var1}'*100) #membuat semua variabel menjadi string f string/format
print(str(var1)*100) 

a= 6
b= "abcd"

print(a+len(b)) #len bertugas mengukur panjang variabel
print(1-2)
print(1/2)
print(1*2)
print(1**2)
print(1%2)

b = "abcdef"

if 1 != 5:
    print('a') #if tidak perlu else
else:
    print('error')

b = input('masukan huruf: ')

if len(b) >= 5:
    print(b)
    if len(b) % 2 == 0:
        print(b * 3)
    elif len(b) >= 10:
        print(b * 5)
else:
    print(b * 10)

n = int (input('masukan nilai: '))

if (n)>100:
    print('Nilai tidak valid')
elif (n)>=90 and (n)<=100:
    print('mantap')
else:
    print('gagal')

arr = ["apple", "jeruk", "kelapa", "pisang"] #array kumpulan variabel
for i in arr:
    print("saya",i)

arr = ["apple", 2, True, None, 9.90] #array bisa di isi campuran namun hanya kusus di python
for i in arr:
    print("saya",i)

#perulangan dalam perulagan
for i in range(0,3):
    print('apel',i)
    for j in range(0,3):
        print('pisang',j)
        for h in range(0,3):
            print('jeruk',h)

for i in range(0,10,2): #2=beda
    print('hai',i)
    if i > 5:
        print('aple',i)
        break

for i in range(0,10): #2=beda
    if i == 5:
        print('aple',i)
        continue
        print('pisang')
    print('hai',i)

a= int (input('masukan angka:'))
while a <=0:
    print('a')
    break

a = True
while a:
    print('a')
    a = False

def tambah(a, b):
    print(a+b)

tambah(1, 4)
tambah(7, 4)
tambah(2, 6)
tambah(2, 5)
tambah(5, 4)

for i in range(0, 9):
    tambah(i,i+2)

def kurang (a, b):
    print(a-b)

kurang(1,10)

for i in range(0,5):
    print('*'*(i+1))

i = 6
while i > 1:
    print('*' * (i - 1))
    i -= 1

i = 0
while i < 5:
    star= '*' * (2*i + 1)
    print(star.center(9))
    i += 1