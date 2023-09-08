a = int(input("Masukkan jummlah baris"))
bintang = "*"
for i in range(a):
    print(" " * (a - i - 1) + bintang)
    bintang += "*"