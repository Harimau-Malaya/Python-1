# arr =["apel", "jeruk", "kelapa", "pisang"]
# arr =["semangka", 2, True, None, 9.90]
# for i in arr:
#     print("Saya ",i)

# perulangan di dalam perulangan
# for i in range(0,3):
#     print('apel', i)
#     for j in range(0,3):
#         print('pisang', j) 
#         for h in range(0,3):
#             print('jeruk', h)

# for i in range(0,10,2):
#     print('hai', i)
#     if i > 5:
#          print('apel', i)
#          break

# for i in range(0,10):
#     if i==5:
#          continue
#          print('apel', i)
#          print('pisang')
#     print('hai', i)

# a = int(input('masukkan angka: '))
# while False:
#     print('a')
#     break

# def tambah(a, b):
#     print(b+a)
# def kurang(a, b):
#     print(b-a)
# def kali(a, b):
#     print(b*a)

# tambah(1, 10)
# kurang(9, 5)
# kali(9,10)

a = 0
while a<5:
    print('*' *(a+1))
    a += 1 

a = 6
while a>1:
    print('*' *(a-1))
    a -= 1

a = 0
while a < 5:
    bintang= '*' *(2*a+1)
    print(bintang.center(9))
    a +=1

a = 0
while a < 5:
    print(''+'*' *(a+1))
    a +=1
