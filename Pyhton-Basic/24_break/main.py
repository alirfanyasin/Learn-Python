# BREAK

# break berfungsi untuk menghentikan suatu statement

# Basic Break ============================
# angka = 0
# while angka < 5:
#   angka += 1
#   if angka == 3:
#     print("heheh")
#     break # statement akan berhenti 
#   print(f"Nilai angka adalah = {angka}")



# Middle Break ===========================
data = int(input("Masukkan Angka : "))
angka  = 0
while True:
  angka += 1
  if angka == data :
    print(f"Selesai")
    break

  print(f"Nilai angka adalah : {angka}")


