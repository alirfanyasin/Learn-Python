# ===================== Copy and Pop Dictionary =====================

data = {
  "nama" : "Irfan Yasin",
  "nim" : 1203220082,
  "umur" : 18,
  "kelas" : "IF-02-02"
}

personal = data.copy()

print(f"data : {data}")
print(f"personal : {personal}")

print("\n")

data["nama"] = "Saipul Kilab" # nama di ubah
print(f"data : {data}")
print(f"personal : {personal}")

print("\n")



# pop dictionary
dataNama = personal.pop("nama") # mengambil data nama dan di keluarkan dari dictionary

print(f"data nama : {dataNama}")
print(f"personal : {personal}") # data nama keluar dari dictionary


print("\n")

# popitem dictionary
dataTerakhir = personal.popitem() # popitem() -> mengambil data terakhir

print(f"data terakhir : {dataTerakhir}") # mengambil item terakhir berupa key dan value bertype tuple
print(f"personal : {personal}")