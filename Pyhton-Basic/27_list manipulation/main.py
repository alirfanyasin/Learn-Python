# =================== List Manipulation ===================


data = ["Irfan", "Yasin", "Achmad"]

# Mengabil data dari list
print(f"data pertama memiliki index 0 = {data[0]}")

# Mengambil data terakhir
print(f"data terakhir adalah = {data[-1]}")


# Mengambil jumlah data list -> len()
print(f"Jumlah data dalam list = {len(data)}")



# Manipulasi data list ========================

# Menambahkan item atau data pada list sesuai posisi -> insert(index, item)
print("\n"+10*"="+" Menambahkan Sesuai Posisi "+"="*10)
data_anggota = ["Ucup", "Dadang", "Randi"]
data_anggota.insert(1, "Asep") # Asep di tambahkan di index ke 1
print(f"Data sesudah di tambahkan = {data_anggota}")


# Menambahkan item atau data di posisii bagian akhir -> append(item)
print("\n"+10*"="+" Menambahkan Di Akhir "+"="*10)
data_anggota.append("Jajang") # Jajang di tambahkan di bagian akhir
print(f"Data ditambahkan di akhir = {data_anggota}")


# Menambahkan atau menggabungkan list dengan list -> extend(item)
print("\n"+10*"="+" Menggabungkan list "+"="*10)

data_lama = ["Stevan", "Alexa", "Janny"]
data_baru = ["Jhon", "Robert", "Sarah"]

data_lama.extend(data_baru) # data_lama di gabungkan dengan data_baru
print(data_lama)


# Merubah data
print("\n"+10*"="+" Merubah data list "+"="*10)
data_lama[2] = "Michael"  # Janny di ubah menjadi Michael
print(data_lama)



# mengahapus data data -> remove(item)
print("\n"+10*"="+" Menghapus data list "+"="*10)
data_lama.remove("Robert") # Robert di hapus
print(data_lama)


# Menghapus data paling akhir -> pop()
print("\n"+10*"="+" Menghapus data akhir list "+"="*10)
data_lama.pop() # Menghapus data akhir yaitu Sarah
print(data_lama)



