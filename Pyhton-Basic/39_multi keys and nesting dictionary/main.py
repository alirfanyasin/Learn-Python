# ========================= Multi Key and Nesting Dictionary =========================

import datetime as dt


mahasiswa1 = {
  'nama' : 'Irfan Yasin',
  'nim' : '1203220082',
  'sks_lulus' : 134,
  'beasiswa' : False,
  'tanggal_lahir' : dt.datetime(2001,4,10)
}
mahasiswa2 = {
  'nama' : 'Randy Saputra',
  'nim' : '1203220102',
  'sks_lulus' : 140,
  'beasiswa' : True,
  'tanggal_lahir' : dt.datetime(2002,10,1)
}
mahasiswa3 = {
  'nama' : 'Achmad Rian',
  'nim' : '1203220034',
  'sks_lulus' : 134,
  'beasiswa' : False,
  'tanggal_lahir' : dt.datetime(2002,8,23)
}

# Nesting Dictionary
data_mahasiswa = {
  'MAH001' : mahasiswa1,
  'MAH002' : mahasiswa2,
  'MAH003' : mahasiswa3,
}


print(f"{'KEY':<7} {'NAMA':<15} {'NIM':<12} {'SKS LULUS':<10} {'BEASISWA':^10} {'TANGGAL LAHIR':<10}")
print("-"*75)

for mhs in data_mahasiswa:
  KEY = mhs
  NAMA = data_mahasiswa[KEY]['nama']
  NIM = data_mahasiswa[KEY]['nim']
  SKS_LULUS = data_mahasiswa[KEY]['sks_lulus']
  BEASISWA = data_mahasiswa[KEY]['beasiswa']
  TANGGAL_LAHIR = data_mahasiswa[KEY]['tanggal_lahir'].strftime("%x")
  print(f"{KEY:<7} {NAMA:<15} {NIM:<12} {SKS_LULUS:<10} {BEASISWA:^10} {TANGGAL_LAHIR:<10}")


  

# Note atau catatan
# KEY merupakan variabel konstanta
# Variabel konstanta ditandai dengan hurup kapital (KEY)

