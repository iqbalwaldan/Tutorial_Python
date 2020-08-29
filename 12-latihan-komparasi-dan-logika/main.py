# episode latihan logika dan komparasi

#membuat gabungan area rentang dari angka

# +++++++3-------10+++++++

inputuser = float(input("masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# +++++++3-------
# memeriksa angka kurang dari 3
isKuraangDari = (inputuser < 3)
print("Kurang Dari 3 =", isKuraangDari)

# -------10+++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputuser > 10)
print("Lebih Dari 10 =", isLebihDari)

# +++++++3-------10+++++++

isCorrect = isKuraangDari or isLebihDari
print("Angka yang anda masukkan:", isCorrect)


# -------3+++++++10-------
# kasus irisan
print("\n",10*"=","\n")
inputuser = float(input("masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# -------3+++++++
# Lebih dari 3
isLebihDari = inputuser > 3
print("Lebih Dari 3 =", isLebihDari)

# +++++++10-------
# kurang dari 10
isKuraangDari = inputuser < 10
print("Kurang Dari 10 =", isKuraangDari)

# -------3+++++++10-------
isCorrect = isKuraangDari and isLebihDari
print("Angka yang anda masukkan:", isCorrect)