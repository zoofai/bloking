import tkinter as tk 
from tkinter import ttk

def hitung():
    angka1 = float(angka1_entry.get())
    angka2 = float(angka2_entry.get())
    operator = operator_combobox.get()

    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    else:
        hasil = "Operator tidak valid"

    hasil_label.config(text=str(hasil))

    window = tk.Tk()
    window.tittle("Kalkulator")

    input_frame = ttk.Frame(window)
    input_frame.pack(padx=10, pady=10)

    angka1_label = ttk.Label(input_frame, text="Angka 1 :")
    angka1_label.grid(row=0, column=0, sticky="W")
    angka1_entry = ttk.Entry(input_frame)
    angka1_entry.grid(row=0, column=1)

    angka2_label = ttk.Label(input_frame, text="Angka 2 :")
    angka2_label.grid(row=0, column=0, sticky="W")
    angka2_entry = ttk.Entry(input_frame)
    angka2_entry.grid(row=0, column=1)

    operator_label = ttk.Label(input_frame, text="Operator:")
    operator_label.grid(row=2, column=0, sticky="W")
    operator_combobox = ttk.Combobox(input_frame, values=["+", "-", "*", "/"])

    hitung_button = ttk.Button(window, text="Hitung", command=hitung)
    hitung_button.pack(pady=10)

    hasil_label = ttk.Label(window, text="Hitung", command=hitung)
    hasil_label.pack()

    window.mainloop()