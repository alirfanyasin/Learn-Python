# FORMAT STRING --> (f)

# Contoh generic
# String
nama = "Jhonsena"
format_str = f"Hello {nama}"
print(format_str)
print("============================")


# Boolean
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)
print("============================")


# Angka
angka = 2005.5
format_str = f"Angka = {angka}"
print(format_str)
print("============================")


# Bilangan Bulat
bilanganBulat = 15
format_str = f"Bilangan bulat = {bilanganBulat:d}" 
print(format_str)
print("============================")


# Bilangan Ribuan
bilanganRibuan = 20000
format_str = f"Bilangan ribuan = {bilanganRibuan:,}" # ribuan (,)
print(format_str)
print("============================")



# Bilangan desimal
angka = 2093.3445
format_str = f"Desimal = {angka:.2f}" #.2f artinya mengambil jumlah angka di belakang koma, dan simbol f artinya (float)
print(format_str)
print("============================")


# Menampilkan leading zero atau di depannya
angka = 2930.392090
format_str = f"Desimal = {angka:08.2f}" # 0 => menambahkan angka 0, 8 => menghitung banyak angkanya, .2f => mengambail angka di belakang koma
print(format_str)
print("============================")



# Menampilkan plus atau minus (+ -)
angka_plus = 10
angka_minus = -10
format_plus = f"Plus = {angka_plus}"
format_minus = f"Minus = {angka_minus}"

# print(format_plus:+d)
# print(format_minus:+d)
print(format_plus)
print(format_minus)
print("============================")



# Memformat persen
persentase = 0.045
format_persen = f"Persen = {persentase:.2%}"
print(format_persen)
print("============================")


# =======================================================================
# Melakukan aritmatikan di dalam kurung ini {...}
harga  = 10000
jumlah = 5
format_str = f"Total = Rp. {harga * jumlah:,}"
print(format_str)
print("============================")


# Format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)





