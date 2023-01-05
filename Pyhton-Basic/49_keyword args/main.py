# ===================== Keyword Args =====================
# contoh (**keyword)

# Contoh tanpa **keyword_args
def fungsi(nama, tinggi, berat):
  print(f"Nama : {nama}, Tinggi : {tinggi}, Berat : {berat}")

fungsi("Ucup", 183, 79)



# Contoh menggunakan **keyword_args
def fungsi(**keyword_args):
  print(keyword_args)
fungsi(nama="Irfan", tinggi=170, berat=60) # outputnya berupa dictionary atau object





def fungsi(**keyword_args):
  # print(keyword_args['nama'])
  nama = keyword_args['nama']
  tinggi = keyword_args['tinggi']
  berat = keyword_args['berat']
  print(f"Nama : {nama}, Tinggi : {tinggi}, Berat : {berat}")

fungsi(nama="Irfan", tinggi=170, berat=60) 


print("\n")

# menggunakan *args dan **keyword_args
def math(*args, **keyword_args):
  output = 0
  if keyword_args['operasi'] == 'jumlah':
    for angka in args:
      output += angka
  elif keyword_args['operasi'] == 'kali':
    output = 1
    for angka in args:
      output *= angka
  else : print("Operasi tidak ada")
  return output

hasil = math(1,2,3,4,5,6,7,8, operasi="jumlah")
print(f"Hasil penjumlahan : {hasil}")
hasil = math(1,2,3,4,5,6,7,8, operasi="kali")
print(f"Hasil perkalian : {hasil}")





