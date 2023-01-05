# Operasi dan Manipulasi string

# 1. Menyambung string (concatenate) menggunakan tanda plus +
nama_pertama = "Al"
nama_tengah = "Irfan"
nama_belakang = "Yasin"
nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_belakang
print(nama_lengkap)
print("============================")


# 2. Menghitung panjang dari string
panjangText = len(nama_lengkap)
print(panjangText)
print("============================")


# 3. Operator untuk string
# 3.a Mengecek apakah ada komponen char atau string di string
namaLengkap = "Al Irfan Yasin"
s = "s" # huruf s ada pada kata Yasin
status = s in namaLengkap
print(status) # hasilnya true
print("============================")


# 3.b Mengecek apakah tidak ada komponen char atau string di string
namaBenda = "Sepeda Motor"
o = "o" # huruf o ada pada kata Motor
status = o not in namaBenda
print(status) # hasilnya false
print("============================")



# 3.c Mengulang string atau looping string
print(10*"wk")
print("Hello"*15)
print("============================")



# 3.d Indexing (mencari huruf menggunakan nomor index)
exampleText = "Hello World"
print("Index ke 6 - ", exampleText[6])
print("Index ke -1 - ", exampleText[-1]) # mengambil dari belakang karena menggunakan minus (-)
print("============================")


# 3.e Mengambil sesuai range (:)
print("Index ke - [1:7] :" + exampleText[1:7])
print("Index ke - [0:7] :" + exampleText[0:7:2]) # meloncati 2 karakter
print("============================")


# 3.f Item paling kecil
print("Paling kecil : " + min(exampleText))
# 3.g Item paling besar
print("Paling besar : " + max(exampleText))
print("============================")


# ASCII
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah :", str(ascii_code))
data_ascii = 114
print("ASCII code untuk huruf r adalah :", chr(data_ascii))
print("============================")



# 4. Operator dalam bentuk method

# a. Mengitung karakter yang sama
exampleText1 = "Irfan Yasin"
jumlah = exampleText1.count("a")
print("Jumlah huruf a pada " + exampleText1 +": "+ str(jumlah))
print("============================")





