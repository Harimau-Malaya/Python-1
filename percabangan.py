b = "abcdef"

if 1 != 5:
    print('a') #if tidak perlu else
else:
    print('error')

b = input('Masukkan Huruf: ')

if len(b) >=5:
    print(b)
    if len(b)%2==0:
        print(b*3)
    elif len(b)>=10:
        print(b*5)
else:
    print(b*10)
        
n = int(input('Masukkan Nilai: '))

if (n)>100:
    print("Nilai Tidak Valid.")
elif (n)>=90 and (n)<=100:
    print("Mantap!")
else:
    print("Gagal.")