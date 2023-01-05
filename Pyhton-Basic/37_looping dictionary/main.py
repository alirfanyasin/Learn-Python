# ======================= Looping Dictionary =======================

data = {
  "nama" : "Irfan Yasin",
  "umur" : 18,
  "nim" : 1203220082,
  "alamat" : "Surabaya"
}



# Looping
for dt in data:
  print(dt) # outputnya berupa key
  # print(data[dt]) # outputnya berupa value




# Operator untuk mengambil item / iterables

# Menggunakan key()
print("\n")
keys = data.keys()
print(keys) # outputnya berupa key


print("\n")
for dt in data.keys():
  print(data.get(dt)) # outputnya berupa value


# Menggunakan values()
print("\n")
values = data.values()
print(values) # outputnya berupa value


print("\n")
for dt in data.values():
  print(dt) # outputnya berupa value



# Menggunakan items()
print("\n")
items = data.items()
print(items) # outputnya berupa key and value -> tuple


print("\n")
for dt in data.items():
  print(dt) # outputnya berupa key and value -> berbentuk tuple


print("\n")
for key,value in data.items():
  print(f"key = {key}, value = {value}")







