# ===================== Latihan List =====================

# Membuat program data buku

list_buku = []

while True:
  print("Masukkan Data Buku")
  judul = input("Judul Buku\t: ")
  penulis = input("Nama Penulis\t: ")

  data_buku = [judul, penulis]
  list_buku.append(data_buku)

  # print("No.\t| Judul\t\t\t | Penulis\t\t ")
  print("\n\n","="*10," Data Buku ",10*"=","\n")
  for index,buku in enumerate(list_buku):
    print(f"{index+1}\t| {buku[0]}\t | {buku[1]}\t\t")

  print("\n","="*20)
  isLanjut = input("Apakah dilanjutkan?(y/n)")

  if(isLanjut == "n"): break

print("Program Selesai")