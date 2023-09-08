user = input("Menghitung [Persegi/Persegi Panjang/Trapesium] : ")

if user == "Persegi" :
    s = int(input("Masukkan Sisi : "))
    print("Hasil Keliling Persegi adalah ", s*4)
    print("Hsil Luas Persegi adalah ", s*s)

elif user == "Persegi Panjang" :
    p = int(input("Masukkan Atas :"))
    t = int(input("Masukkan Tinggi :"))
    print("Hasil Keliling Persegi Panjang adalah ", p+p+t+t)
    print("Hasil Luas Persegi Panjang adalah ", p*t)

elif user == "Trapesium" :
    a = int(input("Massukkan Atas : "))
    b = int(input("Massukkan Bawah : "))
    t = int(input("Massukkan Tinggi : "))
    m1 = int(input("Massukkan Sisi Miring Kanan : "))
    m2 = int(input("Massukkan Sisi Miring Kiri : "))
    print("Hasil Keliling Trapesium adalah " ,a+b+m1+m2)
    print("Hasil Luas Trapesium adalah ",1/2 *(a+b)*t)

else:
    print("Masukkan input yang benar!")