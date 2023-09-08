import tkinter as tk


def hitung_total():
    harga_barang = float(entry_harga.get())
    jumlah_barang = int(entry_jumlah.get())
    total_harga = harga_barang * jumlah_barang
    label_total.config(text=f"Total Harga: Rp {total_harga}")


root = tk.Tk()
root.title("Program Kasir")


label_harga = tk.Label(root, text="Harga Barang:")
label_harga.pack()
entry_harga = tk.Entry(root)
entry_harga.pack()


label_jumlah = tk.Label(root, text="Jumlah Barang:")
label_jumlah.pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()


tombol_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
tombol_hitung.pack()


label_total = tk.Label(root, text="")
label_total.pack()


root.mainloop()