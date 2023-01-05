# =================== List Operation ===================
print("\n"+10*"="+" Menghitung Jumlah Data Tertentu "+"="*10)
data_angka = [1,5,6,2,3,9,3,8,5,0,2,4,6,7,5,2,3,4,6,7,3,5,6]
print(f"Data angka = \n{data_angka}\n")

# Hitung jumlah angka yang tampil -> count(item)
jumlah_data_5 = data_angka.count(5)
jumlah_data_3 = data_angka.count(3)

print(f"Jumlah angka 5 = {jumlah_data_5}")
print(f"Jumlah angka 3 = {jumlah_data_3}")


# Mengambil posisi data -> index(data)
print("\n"+10*"="+" Mengambil Posisi Data "+"="*10)
data = ["Ucup", "Dudung" ,"Asep"]
print(data)
index_dudung = data.index("Dudung")
print(f"'Dudung' ada di index ke = {index_dudung}")

# Mengurutkan List dari kecil ke besar -> sort()
print("\n"+10*"="+" Mengurutkan Data List "+"="*10)
data_angka.sort() # dari kecil ke besar
print(f"Dari kecil ke besar = {data_angka}")
data_angka.reverse() # dari besar ke kecil
print(f"Dari Besar ke Kecil = {data_angka}")
