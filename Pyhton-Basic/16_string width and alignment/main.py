# Width and Multiline

# Data
data_nama = "Irfan Yasin"
data_umur = 18
data_tinggi = 150.1
data_nomor_sepatu = 44

# String Standard
print(7*"="+" String Standard "+"="*7)
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(data_string)


# String Multiline (\n) -> menambahkan enter, atau newline
print("\n"+7*"="+" String Multiline "+"="*7)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print(data_string)


# String Multiline ("""...""") -> kutip triplets
print("\n"+7*"="+" String Kutip Triplets "+"="*7)
data_string = f"""
nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(data_string)


# String Rata Kanan (variabel_name:>5)
print("\n"+7*"="+" String Rata Kanan "+"="*7)
data_string = f"""
nama   = {data_nama:>11}
umur   = {data_umur:>11}
tinggi = {data_tinggi:>11}
sepatu = {data_nomor_sepatu:>11}
"""
print(data_string)


# :> rata kanan
# :< rata kiri
# :^ rata tengah



