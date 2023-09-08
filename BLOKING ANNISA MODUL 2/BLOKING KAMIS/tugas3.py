import tkinter as tk


def simpan_data():
    nama = entry_nama.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    nomor_telepon = entry_nomor_telepon.get()
    alamat = entry_alamat.get()

    
    print("Data Siswa Baru:")
    print("Nama:", nama)
    print("Tanggal Lahir:", tanggal_lahir)
    print("Asal Sekolah:", asal_sekolah)
    print("NISN:", nisn)
    print("Nama Ayah:", nama_ayah)
    print("Nama Ibu:", nama_ibu)
    print("Nomor Telepon:", nomor_telepon)
    print("Alamat:", alamat)


def hapus_inputan():
    entry_nama.delete(0, tk.END)
    entry_tanggal_lahir.delete(0, tk.END)
    entry_asal_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_nama_ayah.delete(0, tk.END)
    entry_nama_ibu.delete(0, tk.END)
    entry_nomor_telepon.delete(0, tk.END)
    entry_alamat.delete(0, tk.END)


window = tk.Tk()
window.title("Data Siswa Baru")


label_nama = tk.Label(window, text="Nama Lengkap:")
entry_nama = tk.Entry(window)

label_tanggal_lahir = tk.Label(window, text="Tanggal Lahir:")
entry_tanggal_lahir = tk.Entry(window)

label_asal_sekolah = tk.Label(window, text="Asal Sekolah:")
entry_asal_sekolah = tk.Entry(window)

label_nisn = tk.Label(window, text="NISN:")
entry_nisn = tk.Entry(window)

label_nama_ayah = tk.Label(window, text="Nama Ayah:")
entry_nama_ayah = tk.Entry(window)

label_nama_ibu = tk.Label(window, text="Nama Ibu:")
entry_nama_ibu = tk.Entry(window)

label_nomor_telepon = tk.Label(window, text="Nomor Telepon:")
entry_nomor_telepon = tk.Entry(window)

label_alamat = tk.Label(window, text="Alamat:")
entry_alamat = tk.Entry(window)


tombol_simpan = tk.Button(window, text="Simpan", command=simpan_data)
tombol_hapus = tk.Button(window, text="Hapus", command=hapus_inputan)


label_nama.grid(row=0, column=0)
entry_nama.grid(row=0, column=1)

label_tanggal_lahir.grid(row=1, column=0)
entry_tanggal_lahir.grid(row=1, column=1)

label_asal_sekolah.grid(row=2, column=0)
entry_asal_sekolah.grid(row=2, column=1)

label_nisn.grid(row=3, column=0)
entry_nisn.grid(row=3, column=1)

label_nama_ayah.grid(row=4, column=0)
entry_nama_ayah.grid(row=4, column=1)

label_nama_ibu.grid(row=5, column=0)
entry_nama_ibu.grid(row=5, column=1)

label_nomor_telepon.grid(row=6, column=0)
entry_nomor_telepon.grid(row=6, column=1)

label_alamat.grid(row=7, column=0)
entry_alamat.grid(row=7, column=1)

tombol_simpan.grid(row=8, column=0)
tombol_hapus.grid(row=8, column=1)


window.mainloop()