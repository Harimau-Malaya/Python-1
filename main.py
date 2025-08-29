var = "1"
var2 = "halo"
print(f'{var}'*100)
print(str(var)*100)


print(1+2)
print(1-2)
print(1/2)
print(1*2)
print(1**2)
print(1%2)



b = input('masukkan huruf: ')

if len(b) >= 5:
    print(b)
    if len(b)%2==0:
        print(b*3)
    elif len(b)>=10:
        print(b*5)
    else:
        print(b*10)


n = int(input('masukkan nilai: '))

if (n)>100:
    print ("Nilai tidak valid")
elif (n)>=90 and (n)<=100:
    print("Mantap!")
else:
    print("Gagal")
    
arr = ["apel", "jeruk", "kelapa", "pisang"] 
for i in arr:
    print("saya ", i)

arr = ["apel", 2, True, None, 9.90]
for i in arr:
    print("saya ", i)


for i in range (0,3):
    print('x')
    for j in range(0,3):
        print('z')


for i in range(0,3):
    print('apel ', i)
    for j in range(0,3):
        print('pisang ', j)
        for h in range(0,3):
            print('jeruk', h)


for i in range(0,10,2):
    print('hai', i)
    if i > 5:
        print('apel', i)
        break 


for i in range(0,10):
    if i==5:
        continue
        print('apel')
        print('pisang')
    print('hai', i)


a = int (input('masukkan angka: '))
while a <=0:
    print('a')
    break

a = True
while a:
    print('a')
    a = False



def tambah(a):
    print('hai', a)

tambah('apel')

def tambah(a, b):
    print(b+a)

tambah(1, 10)

def tambah(a, b):
    print(b+a)
def kurang(a, b):
    print(b-a)
def kali(a, b):
    print(b*a)

tambah(1,  10)
kurang(9, 5)
kali(9, 10)                                                  


for i in range(0, 5):
    print('*'*(i+1))

i = 6
while i > 1:
    print('*' *(i - 1))
    i -= 1

i = 5
while i > 0:
    print('*' * i)
    i -= 1

i = 0
while i < 5:
    bintang = '*' *(2 * i + 1 )
    print(bintang.center(9))
    i += 1 


