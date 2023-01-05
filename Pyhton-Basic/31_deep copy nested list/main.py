# ================= DEEP COPY NESTED LIST =================

data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0, data_1]
print(f"Data = {data_2d}")


# Mengambil data di list dua dimensi
# data = data_2d[0][1]
# print(data)



# Mengambil semua address
data_2d_copy = data_2d.copy()
print(f"Address asli = {hex(id(data_2d))}") # 0x229c0cc1900
print(f"Address copy = {hex(id(data_2d_copy))}") # 0x229c0c812c0

print("\n")
print("Address dari member ke-1")
print(f"Address asli = {hex(id(data_2d[0]))}") # 0x198c79a3680
print(f"Address copy = {hex(id(data_2d_copy[0]))}") # 0x198c79a3680

print("\n")
data_2d[1][0] = 5
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")







print("\n")
print(10*"="+" Deep Copy "+"="*10)

# Menggunakan deepcopy()

from copy import deepcopy

data_2d = [data_0, data_1, 10]
data_2d_deepcopy = deepcopy(data_2d)

print(f"Address asli = {hex(id(data_2d))}") # 0x229c0cc1900
print(f"Address copy = {hex(id(data_2d_deepcopy))}") # 0x229c0c812c0


print("\n")
print("Address dari member ke-1")
print(f"Address asli = {hex(id(data_2d[0]))}") # 0x198c79a3680
print(f"Address copy = {hex(id(data_2d_deepcopy[0]))}") # 0x198c79a3680

print("\n")
data_2d[1][0] = 20
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")
print(f"data deepcopy = {data_2d_deepcopy}")


