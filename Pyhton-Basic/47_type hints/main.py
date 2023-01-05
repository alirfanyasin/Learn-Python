# ================== Type Hint Function ==================

# Contoh yang salah
# def fungsi(parameter):
#   print(parameter**2)

# fungsi(2)
# fungsi("Irfan")
# fungsi(True)


# Contoh yang benar
# menggunakan return
def function(argument:int) -> int:
  output = 10**argument
  return output

HASIL = function(2)
print(HASIL)



# tanpa menggunaakn return
def display(argument:str):
  print(argument)

display("Irfan")
