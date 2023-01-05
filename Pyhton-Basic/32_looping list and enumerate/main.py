# ================ Looping List ================

# for loop
print(5*"="+" For Loop "+"="*5)

kumpulan_angka = [1,2,4,2,3,6,8,0,9,5,3]
for num in kumpulan_angka:
  print(f"angka = {num}") 



print("\n")




peserta = ["Ucup", "Dudung", "Asep", "Toni"]
for nama in peserta:
  print(f"Nama\t: {nama}")



# foor loop and range()
print("\n")
print(5*"="+" For Loop and Range "+"="*5)
kumpulan_angka = [10,23,3,2,35,82,2,0,4,2,13,25]
panjang = len(kumpulan_angka)

for i in range(panjang):
  # print(f"Angka = {i}") -> mengambil index
  print(f"Angka = {kumpulan_angka[i]}")





# While Loop
print("\n")
print(5*"="+" While Loop "+"="*5)

kumpulan_angka = [1,4,5,46,23,1,7,94,74]
panjang = len(kumpulan_angka)
i=0
while i < panjang:
  print(f"angka = {kumpulan_angka[i]}")
  i += 1





# List Comprehension
print("\n")
print(5*"="+" List Comprehension "+"="*5)
data = ["Ucup", 23, 9, "Dudung", 2, 4, "Asep"]
[print(f" data = {i}") for i in data]

# angka kuadrat
angka = [10,2,43,23,56,9,20]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)



# Enumerate
print("\n")
print(5*"="+" Enumerate "+"="*5)
data_list = ["Ucup", 23, 9, "Dudung", 2, 4, "Asep"]

for index,data in enumerate(data_list):
  print(f"index = {index}, data = {data}")