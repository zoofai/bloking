user = input("Menghitung[Tabung/Balok] : ")

if user == "Tabung" :
    t = int(input("Masukkan Tinggi : "))
    j = int(input("Masukkan Jari-jari : "))
    vol = 22/7*j*j*t
    print("Volume Tabung : ")

elif user == "Balok" :
    p = int(input("Masukkan Panjang : "))
    l = int(input("Masukkan Lebar : "))
    t = int(input("Masukkan Tinggi : "))
    print("Volume Balok : ",p*l*t)

else:
    print("Tidak ada didaftar")
