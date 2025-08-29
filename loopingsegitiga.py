for i in range(0, 5):
    print('*'*(i+1))
    
a = 0
b = int(input("Masukkan Batas: "))
while a < b:
    print('*'*(a+1))
    a += 1
    
a = 0
b = int(input("Masukkan Batas: "))
while a < b:
    print('*'*b)
    b -= 1
    
a = int(input("Masukkan Angka: "))
a = 0
while a < 5:
    stars = '*' * (2 * a + 1)
    print(stars.center(9))
    a += 1