# =========================== Anonymous & Lambda Function ===========================

# Lambda Function
kuadrat = lambda angka : angka**2
print(kuadrat(2))

pangkat = lambda num,pow : num**pow
print(f"Hasilnya : {pangkat(2, 3)}")


# Sorting list biasa
data_list = ["Otong","Ucup","Dadang"]
data_list.sort()
print(data_list)


# sorting list berdasarkan panjang karakter
data_list = ["Otong", "Ucup", "Dadang"]
data_list.sort(key=len)
print(data_list)


# Sorting menggunakan lambda
data_list = ["Otong", "Ucup", "Dadang"]
data_list.sort(key=lambda nama : len(nama))
print(data_list)



# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

# cara 1
def kurang_dari_lima(angka):
  return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print(data_angka_baru)

# cara 2
data_angka_baru = list(filter(lambda x : x<7, data_angka))
print(data_angka_baru)


# studi kasus mengambil angka genap
data_genap = list(filter(lambda genap : genap % 2 == 0, data_angka))
print(data_genap)


# studi kasus mengambil angka ganjil
data_ganjil = list(filter(lambda ganjil : ganjil % 2 != 0, data_angka))
print(data_ganjil)





# Anonymous Function
# currying <- Haskel Curry

def pangkat(n):
  return lambda angka : angka**n

pangkat_2 = pangkat(2)
print(pangkat_2(5)) # output 5 pangkat 2 = 25

print(pangkat(2)(10)) #outpu 10 pangkat 2 = 100
