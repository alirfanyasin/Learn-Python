# Continue, Pass

# ==================================
# Continue
# ==================================
# Continue berfungsi untuk melangkahi suatu urutan perulangan
angka = 0
while angka < 5:
  angka += 1
  if angka == 3: 
    print("Hehe")
    continue
  print(f"Angka sekarang adalah {angka}")



# ==================================
# Pass -> dia berfungsi sebagai dummy, tidak akan di eksekusi
# ==================================
# angka = 0
# while angka < 5:
#   angka += 1
#   if angka == 3 : pass # pass tidak akan di eksekusi
#   print(angka)