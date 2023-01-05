#======================== LIST ========================

# Kumpulan data
# data integer
data_integer = [1,2,3]
print(data_integer)

# data string
data_string = ["Irfan", "Yasin", "Ahmad"]
print(data_string)

# data boolean
data_bool = [True, False]
print(data_bool)

# =====================================================
print(10*"="+" Data Campuran "+"="*10)
# Data Campuran
data_campuran = [1, "Irfan Yasin", True]
print(data_campuran)

# =====================================================
print(10*"="+" Menggunakan Range "+"="*10)
# Cara alternatif membuat list
data_range = range(0,10,2) # range(start, stop, step)
print(data_range)
data_list = list(data_range) # meng casting menjadi list
print(data_list)


# =====================================================
print(10*"="+" Menggunakan For Loop "+"="*10)
# Membuat list menggunakan for loop
data_list_use_for = [i**2 for i in range(0,10)] # di kuadrat 2 menggunakan (**2)
print(data_list_use_for)

# =====================================================
print(10*"="+" Menggunakan For and If "+"="*10)
# Membuat list menggunakan for dan if
data_list_use_if = [i for i in range(0,10) if i != 5 ] # menghilangkan angka 5
print(data_list_use_if)

# =====================================================
print(10*"="+" Menggunakan For and If Genap "+"="*10)
# Membuat list menggunakan for dan if
data_list_use_if = [i for i in range(0,10) if i % 2 == 0 ] # menampilkan angka genap
print(data_list_use_if)

# =====================================================
print(10*"="+" Menggunakan For and If Ganjil "+"="*10)
# Membuat list menggunakan for dan if
data_list_use_if = [i**2 for i in range(0,10) if i % 2 == 1 ] # menampilkan angka ganjil dan di kuadratin
print(data_list_use_if)



