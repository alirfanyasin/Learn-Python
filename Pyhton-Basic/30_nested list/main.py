# ================== NESTED LIST ==================

data_list_biasa = [1,2,3,4,5]
print(f"List biasa = {data_list_biasa}")

data_0 = [1,2,3]
data_1 = [4,5,6]

list_2d = [data_0, data_1, 7,8]
print(f"List 2D = {list_2d}")

# Contoh penggunaan
peserta_0 = ["Ucup",25,"Laki-laki"]
peserta_1 = ["Dudung",20,"Laki-laki"]
peserta_2 = ["Fitri",21,"Perempuan"]

print("=======================================\n")

data_peserta = [peserta_0, peserta_1, peserta_2]
print(f"Data Peserta = {data_peserta}")

print("=======================================\n")

for peserta in data_peserta:
  print(f"Nama\t: {peserta[0]}")
  print(f"Umur\t: {peserta[1]}")
  print(f"Gender\t: {peserta[2]}\n")


