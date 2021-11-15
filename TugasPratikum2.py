a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua : "))
c = int(input("Masukkan angka ketiga : "))

if (a > b |  a > c):
    print ("bilangan terbesar", a)
if b > a | b > c:
    print ("bilangan terbesar", b)
else:
    print("bilangan terbesar", c)

