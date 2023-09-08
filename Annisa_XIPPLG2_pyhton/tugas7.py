nama = input("Masukkan Nama : ")
gaji = int(input("Masukkan Gaji Pokok :"))
           
tunjangan = 20/100 * gaji
pajak = 15/100 * (gaji+tunjangan)
gajiBersih = int(gaji+ tunjangan - pajak)

print ("---------------------------------")
print("Nama :",nama)
print("Gaji Pokok : ", gaji)
print("Gaji Besar :",gajiBersih)