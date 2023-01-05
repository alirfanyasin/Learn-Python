
def jumlah(*args) :
  hasil = 0
  for angka in args : 
    hasil += angka
  
  return hasil


def kali(*args) :
  hasil = 1
  for num in args : 
    hasil *= num
  return hasil


def pangkat(n:int):
  return lambda angka : angka**2