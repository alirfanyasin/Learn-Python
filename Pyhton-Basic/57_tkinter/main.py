# GUI - Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()

window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Hello World")


NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True) # Menggunakan pack

# komponen-komponen
# 1. Label Nama Depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10, fill="x", expand=True)
# 1. Entry Nama Depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 1. Label Nama Belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang")
nama_belakang_label.pack(padx=10, fill="x", expand=True)
# 1. Entry Nama Belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# Tombol
def tombol_click():
  '''fungsi tombol click'''
  pesan = f"Hai, nama saya {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
  showinfo(title="Hello World", message=pesan)
  

botton_submit = ttk.Button(input_frame, text="Submit", command=tombol_click)
botton_submit.pack(fill="x", expand=True, pady=10, padx=10)


window.mainloop() # membuka window

