# ===================== *args pada fungsi =====================

# Contoh tanpa *args

def fungsi(nama, tinggi, berat) :
  print(f"Nama : {nama}, Tinggi : {tinggi}, Berat : {berat}")

fungsi("Irfan", 170, 60)


def fungsi(data_list):
  data = data_list.copy()
  nama = data[0]
  tinggi = data[1]
  berat = data[2]
  print(f"Nama : {nama}, Tinggi : {tinggi}, Berat : {berat}")

fungsi(["Ucup", 167, 50]) # disini perlu menggunakan braket list



# Menggunakan *args

def function(*args) :
  nama = args[0]
  tinggi = args[1]
  berat = args[2]
  print(f"Nama : {nama}, Tinggi : {tinggi}, Berat : {berat}")

function("Dadang", 176, 64) # disini tidak perlu menggunakan braket list



print("\n")

# Studi Kasus
def tambah(*data):
  #  *data tipenya tuple
  output = 0
  for angka in data:
    output += angka
  
  return output

hasil = tambah(1,2,3,4,5,6,7,8)
print(hasil)


hasil = tambah(10,5,15)
print(hasil)
