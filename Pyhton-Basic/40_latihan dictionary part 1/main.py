# TEMPLATE DICTIONARY MAHASISWA

import datetime as dt
import os

mahasiswa_template = {
  'nama' : 'nama',
  'nim' : '0000000000',
  'sks_lulus' : 0,
  'lahir' : dt.datetime(1111,1,11)
}

data_mahasiswa = {}

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
print(mahasiswa)