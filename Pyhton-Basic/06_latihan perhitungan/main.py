# PROGRAM KONVERSI CELCIUS KE SATUAN LAIN

print("\nPROGRAM KONVERSI CELCIUS\n")
# Celcius
celcius = float(input("Masukkan suhu dalam satuan celcius : "))
print("suhu adalah ", celcius, " Celcius")

# Reamur
reamur = (4/5) * celcius
print("suhu adalah ", reamur, " Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu adalah ", fahrenheit, " Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu adalah ", kelvin, " Kelvin")
