# ====================== Import Statement ======================

# fungsinya untuk mengambil program dari luar
# atau mengambil file external

# 1. Untuk menyambung program dari file external
import main_second # output "hello world" yang diambil dari file main_second.py


# 2. import dengan data
import main_three
print(main_three.data) # cara mengambilnya


# 3. impot dengan fungsi
import main_four
hasil = main_four.fungsi(2,3)
print(hasil)