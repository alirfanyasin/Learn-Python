# =========================== Latihan Fungsi ===========================

import os
# # program luas dan keliling persegi panjang


# # Membuat header program
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print("-"*40)


# # Mengambil input user
# PANJANG = int(input("Masukkan nilai panjang : "))
# LEBAR = int(input("Masukkan nilai lebar : "))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)


# # Tampilkan hasilnya
# print(f"Hasil luas : {LUAS}")
# print(f"Hasil keliling : {KELILING}")







# ====================== Membuat dengan Fungsi ======================

def header() :
  os.system("cls")
  print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
  print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
  print("-"*40)


def input_user() :
  panjang = int(input("Masukkan nilai panjang : "))
  lebar = int(input("Masukkan nilai lebar : "))
  return panjang, lebar


def hitung_luas(lebar, panjang) :
  return lebar*panjang


def hitung_keliling(lebar, panjang) :
  return 2*(lebar+panjang)


def display(message, value) :
  print(f"Hasil perhitungan {message} = {value}")


def opsi(LEBAR, PANJANG) :
  print(10*"-"+" Pilih Perhitungan "+"-"*10)
  print("""
  1. Hitung Luas
  2. Hitung Kuliling
  """)
  option = input("Masukkan pilihan : ")

  if option == "1" : 
    LUAS = hitung_luas(LEBAR, PANJANG)
    display("luas", LUAS)
  elif option == "2": 
    KELILING = hitung_keliling(LEBAR, PANJANG)
    display("keliling", KELILING)
  else : print("Pilihan tidak tersedia")

  return option



while True :
  header()
  LEBAR, PANJANG = input_user()
  opsi(LEBAR,PANJANG) 
  
  isContinue = input("Apakah lanjut (y/n) ? : ")
  if isContinue == "n" : break

print("Terimakasih")


