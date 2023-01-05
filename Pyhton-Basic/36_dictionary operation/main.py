# ====================== Dictionary Operation ======================

data_dict = {
  "nama" : "Ucup",
  "alamat" : "Surabaya",
  "umur": 18 
}


# Panjang dictionary
# nama variabel uppercase
LENDICT = len(data_dict)
print(f"Panjang dictionary : {LENDICT}")


# Mengecek key ada atau tidak
KEY = "nama"
CHECKKEY = KEY in data_dict

print(f"Apakah {KEY} ada di data_dict : {CHECKKEY}")



# Mengakses value (read) dengan menggunakan get
print(data_dict["nama"])
print(data_dict.get("umur")) # cara yang benar
print(data_dict.get("nik", "key tidak ditemukan")) # membuat error



# Mengupdate Data
data_dict["nama"] = "Hello World"
print(data_dict)

data_dict.update({"umur" : 20}) # ketika key nya ada maka data di update
print(data_dict)

# menambah data
data_dict.update({"nomor" : 6287859967039}) # ketika key nya tidak ada maka  data di add
print(data_dict)



# Delete data -> del 
del data_dict["nomor"]
print(data_dict)



