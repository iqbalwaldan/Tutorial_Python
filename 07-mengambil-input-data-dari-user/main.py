# Episode Input dari User

# data yang dimasukkan pasti string
data = input("Masukkan nama: ")
print("Nama = ", data, "Type = ", type(data))

# Jika ingin mengambil data integer
angka1 = int(input("Masukkan angka: "))
print("Angka = ", angka1, "Type = ", type(angka1))

angka2 = float(input("Masukkan angka: "))
print("Angka = ", angka2, "Type = ", type(angka2))

# Jika Boolean
biner = bool(int(input("Masukkan nilai boolean: ")))
print("Boolean = ", biner, "Type = ", type(biner))
