# Calculator

num1 = float(input("Masukkan angka pertama \t\t\t: "))
num2 = float(input("Masukkan angka kedua \t\t\t: "))
opr = input("Masukkan operasi hitung (+,-,*,/,%) \t: ")

if opr == "+" :
  print(f"Hasilnya : {int(num1 + num2)}")
elif opr == "-":
  print(f"Hasilnya : {int(num1 - num2)}")
elif opr == "*":
  print(f"Hasilnya : {int(num1 * num2)}")
elif opr == "/":
  hasil = num1 / num2
  print(f"Hasilnya : {hasil:.2f}")
elif opr == "%":
  hasil = num1 % num2
  print(f"Hasilnya : {int(hasil)}")
else:
  print("Operasi hitung salah")

print("Terimakasih")