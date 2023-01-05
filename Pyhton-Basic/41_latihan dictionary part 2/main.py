# TEMPLATE DICTIONARY MAHASISWA

import datetime as dt
import os
import string
import random

mahasiswa_template = {
  'nama' : 'nama',
  'nim' : '0000000000',
  'sks_lulus' : 0,
  'lahir' : dt.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
  os.system("cls")

  print(f"{'SELAMAT DATANG':^30}")
  print(f"{'DATA MAHASISWA':^30}")
  print("-"*30)

  mahasiswa = dict.fromkeys(mahasiswa_template.keys())
  mahasiswa['nama'] = input("Masukkan nama : ")
  mahasiswa['nim'] = input("Masukkan nim : ")
  mahasiswa['sks_lulus'] = int(input("Masukkan sks lulus : "))

  TAHUN_LAHIR = int(input("Masukkan tahun lahir (YYYY) : "))
  BULAN_LAHIR = int(input("Masukkan bulan lahir (1-12) : "))
  TANGGAL_LAHIR = int(input("Masukkan tanggal lahir (1-31) : "))
  mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

  KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(5)))

  data_mahasiswa.update({KEY:mahasiswa})

  print("\n")

  print(f"{'Key':<6} {'Nama':<10} {'NIM':<10} {'SKS':<5} {'Tanggal Lahir':<10}")
  print("-"*50)

  for mhs in data_mahasiswa :
    KEY = mhs
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<10} {NIM:<10} {SKS:<5} {LAHIR:<10}")

  print("\n")
  is_done = input("Apakah mau di lanjut (y/n)?")
  if is_done == "n" : break

print("Terimakasih")
