# OPERASI LOGIKA ATAU BOOLEAN

# not, or, and, xor

# NOT
print("==========NOT==========")
a = True
c = not a
print("data a =", a)
print('--------Not')
print('data c =', c)


# OR (Jika salah satu ketemu true maka hasilnya true)
print("==========OR==========")
a = False
b = False
c = a or b
print(a, "OR", b, "=" ,c)
a = False
b = True
c = a or b
print(a, "OR", b, "=" ,c)
a = True
b = False
c = a or b
print(a, "OR", b, "=" ,c)
a = True
b = True
c = a or b
print(a, "OR", b, "=" ,c)

# AND (Jika ketemu false maka hasilnya false )
print("==========AND==========")
a = False
b = False
c = a and b
print(a, "AND", b, "=" ,c)
a = False
b = True
c = a and b
print(a, "AND", b, "=" ,c)
a = True
b = False
c = a and b
print(a, "AND", b, "=" ,c)
a = True
b = True
c = a and b
print(a, "AND", b, "=" ,c)

# XOR (Jika nilainya sama maka hasilnya selalu false)
print("==========XOR==========")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=" ,c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=" ,c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=" ,c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=" ,c)
