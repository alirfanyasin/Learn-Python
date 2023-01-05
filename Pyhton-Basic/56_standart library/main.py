# ======================= Standart Library =======================
from datetime import datetime as dt # Library

waktu = dt.now()
print(f"Waktu saat ini : {waktu}")
print(f"Tahun saat ini : {waktu.year}")
print(f"Hari saat ini : {waktu.strftime('%A')}")




# Menghitung data
from collections import Counter

data = ["a","b","c","d","e","f","a","b","c","a","b"]


data_count = Counter(data)
print(data_count)
print(f"jumlah a : {data_count['a']}")



# Cara manual tanpa library
# count = 0
# for i in data:
#   if i == "a":
#     count += 1 

# print(count)



# Mmebaca file
import io 

file = io.open("file_text.txt","r")
print(file.read())
