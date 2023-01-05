# Date and Time

import datetime as dt

# Menampilkan Hari ini
# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"hari ini adalah hari = {hari_ini:%A}")

# =====================================
# tanggal = dt.date(2004,3,13)
# print(tanggal)

# =====================================


# ====== PROGRAM MENGHITUNG UMUR ======
print("Silahkan masukkan tanggal, bulan, tahun lahir anda : \n")
tanggal = int(input("Tanggal\t: "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun \t: "))
tanggal_lahir = dt.date(tahun, bulan, tanggal)

print(f"Tanggal Lahir anda : {tanggal_lahir}")
print(f"Hari lahir anda : {tanggal_lahir:%A}")

today = dt.date.today()
umur_hari = today - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Umur anda sekrang adalah : {umur_tahun} tahun, {umur_bulan} bulan")

