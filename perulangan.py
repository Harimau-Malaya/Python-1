arr = ["apel", "jeruk", "kelapa", "pisang"] #array itu sama aja kumpulan variabel
for i in arr:
    print("Saya", i)

arr = ["apel", 2, True, None, 9.90] #di python array bisa dicampur tipe datanya tapi kalo di bahasa lain ngga bisa
for i in arr:
    print("Saya", i)

#perulangan bersarang
for i in range(0,3):
    print('apel', i)
    for j in range(0,3):
        print('pisang', j)
        for h in range(0,3):
            print('jeruk', h)
            
for i in range(0,10):
    print('apel', i)
    break #buat ngestop perulangannya

for i in range(0,10,2): #2 itu beda jarak lompat
    print('hai', i)
    if i > 5:
        print('apel', i)
        break
    
for i in range(0,10):
    if i==5:
        print('apel', i)
        #continue #buat ngeskip lanjut ke perulangan berikutnya
        print('pisang')
    print('hai', i)

a = int(input("Masukkan Angka: "))
while a <=0:
    print('a')
    break

a = True
while a:
    print('a')
    a = True

def tambah(a, b):
    print(a+b)
    
tambah(1, 4)
tambah(7, 4)
tambah(2, 6)
tambah(2, 5)
tambah(5, 4)

for i in range(0, 9):
    tambah(i, i+2)
    
def tambah(a, b):
    print("Hai", a)
    print("Hai", b)
    
tambah(3, 5)

def tambah(a, b):
    print(b+a)
def kurang(a, b):
    print(b-a)
def kali(a, b):
    print(b*a)
    
tambah(4, 5)
kurang(4, 5)
kali(4, 5)