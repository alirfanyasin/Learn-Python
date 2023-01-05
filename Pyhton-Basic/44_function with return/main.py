# ====================== Function with Return ======================

# Membuat fungsi kuadrat
def kuadrat(x) :
  hasil = x**2
  return hasil

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)


# Fungsi Tambah
def tambah(angka_1, angka_2) :
  return angka_1 + angka_2 # langsung mengembalikan nilai

hasil = tambah(10, 24)
print(hasil)



# Fungsi mereturn banyak nilai
def operasi_matematika(angka_1, angka_2) :
  tambah = angka_1 + angka_2
  kurang = angka_1 - angka_2
  kali = angka_1 * angka_2
  bagi = angka_1 / angka_2

  return tambah, kurang, kali, bagi

k, l, m, n = operasi_matematika(50, 23)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n:.2f}")

