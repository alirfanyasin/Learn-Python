# OPERASI DAN MANIPULASI STRING PART 2
# METHOD STRING

# ================= Merubah Case Dari String =================
# 1. Upper case
print("================ Upper case ================")
exampleText = "hello world" # lower case
print("normal = " + exampleText)
string = exampleText.upper()
print("upper = " + string)


# 2. Lower case
print("================ Lower case ================")
exampleText = "HELLO World"  # upper case
print(f"normal = {exampleText}")
string = exampleText.lower()
print(f"Lower = {string}")



# ================= Pengecekan dengan is X method =================
# Pengecekan Lower case (hasilnya boolean)
print("================ islower and isupper ================")
exampleText = "hello world"
apakah_lower = exampleText.islower() # hasilnya boolean
print(exampleText + " is lower = " + str(apakah_lower))
apakah_upper = exampleText.isupper() # hasilnya boolean
print(exampleText + " is lower = " + str(apakah_upper))


'''
  1. isalpha()   => mengecek huruf saja
  2. isalnum()   => mengecek huruf dan angka
  3. isdecimal() => mengecek angka saja
  4. isspace()   => mengecek spasi, tab, newline \n
  5. istitle()   => mengecek semua kata yang dimulai dengan huruf besar
'''
print("================ isalpha ================")
exampleText = "HelloWorld"
text = exampleText.isalpha()
print(exampleText + " Apakah ini huruf semua = " + str(text))


print("================ isalnum ================")
exampleText = "HelloWorld123"
text = exampleText.isalnum()
print(exampleText + " Apakah ini huruf dan angka = " + str(text))


print("================ isdecimal ================")
exampleText = "12392083"
text = exampleText.isdecimal()
print(exampleText + " Apakah ini angka semua = " + str(text))


print("================ isspace ================")
exampleText = "hello world"
text = exampleText.isspace()
print(exampleText + " Apakah ada sebuah spasi = " + str(text))


print("================ istitle ================")
exampleText = "Hello"
text = exampleText.istitle()
print(exampleText + " Apakah huruf depannya capital = " + str(text))



