# =================== Default Argument Function ===================

# Contoh dan perbedaan
# def function(argument)
# def function(argument = nilai default)

# Contoh 1
def fungsi(nama = "Nathanael Wijaya") :
  print(f"Hello, {nama} selamat datang")

fungsi() # output menggunakan default argument
fungsi("Irfan Yasin") # output menggunakan nilai input argument


# Contoh 2
def hitung_pangkat(angka, pangkat = 3) :
  return angka**pangkat

print(hitung_pangkat(4, 2)) # cara pertama

hasil = hitung_pangkat(pangkat = 2, angka = 5) #cara kedua  
print(hasil)

