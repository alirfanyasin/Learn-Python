# ====================== Function with Argument ======================
'''
Contoh Struktur Fungsi

def function_name(argument):
  # badan fungsi
'''

# Function Sederhana
def hello_world(nama) : 
  print(f"Selama datang {nama}")

hello_world("Irfan Yasin")


# Function Penjumlahan
print("\n")
print("Fuction Penjumlahan")

def penjumlahan(angka_1, angka_2) :
  hasil = angka_1 + angka_2
  print(f"{angka_1} + {angka_2} = {hasil}")

penjumlahan(10, 23)
penjumlahan(20, 40)


# Function Daftar Mahasiswa
print("\n")

def mahasiswa(nama_mahasiswa):
  data_mahasiswa = nama_mahasiswa.copy()
  for mhs in data_mahasiswa : 
    print(f"Selamat Datang {mhs}")


nama_mahasiswa = ["Irfan Yasin", "Nathanael Wijaya", "Moh. Hafiz"]
mahasiswa(nama_mahasiswa)





