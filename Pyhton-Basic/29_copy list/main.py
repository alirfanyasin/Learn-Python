# ================== Copy List ==================

a = ["ucup", "Dudung", "Asep"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# Merubah member dari a
# ketika mengubah list a maka list b akan ikut berubah begitu sebaliknya
a[1] = "Michael"
b.sort()

print(f"A = {a}")
print(f"B = {b}")


# Address dari kedua list a dan b
# Ternyata ouput yang dihasilkan sama
print(f"address a = {hex(id(a))}") # 0x1830f772a80
print(f"address b = {hex(id(b))}") # 0x1830f772a80

# ==========================================================
print("====================================================\n")

# Mengcopy atau menduplikat sebuah list menggunakan -> copy()
c = a.copy()
c[0] = "Irfan"

print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")
print(f"address a = {hex(id(a))}") # 0x1830f772a80
print(f"address b = {hex(id(b))}") # 0x1830f772a80
print(f"address c = {hex(id(c))}") # 0x1fcc4ea18c0

