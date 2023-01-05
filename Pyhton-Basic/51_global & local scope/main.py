# ========================== Global dan Local Scope ==========================

nama = "Dadang" # variabel global

def fungsi():
  print(f"Menampilkan si nama : {nama}")
  tinggi = 180 # variabel local

fungsi() # true
print(tinggi) # error