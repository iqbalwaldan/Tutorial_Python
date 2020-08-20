# Kita belajar casting
# Merubah dari suatu tipe data ke tipe data lain
# type data = int, float, str, bool

## INTEGER
print("====INTEGER====")
data_int = 9
print("data = ", data_int, "type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika bernilai = 0
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool))

## FLOAT
print("====FLOAT===")
data_float = 9.9
print("data = ",data_float, "type = ", type(data_float))

data_int = int(data_float) # dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # false jika nilai = 0 
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_str, "type = ", type(data_str))
print("data = ", data_bool, "type = ", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = False # jika True nilai int dan Float = 1, jika False = 0 
print("data = ", data_bool, "type = ", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool) 
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_str, "type = ", type(data_str))

## STRING
print("====TRING====")
data_str = ""
print("data = ", data_str, "type = ", type(data_str))

data_int = int(data_str) # String berupa angka
data_float = float(data_str) # String Berupa angka
data_bool = bool(data_str) # Jika ingin false data harus kosong
print("data = ", data_int, "type = ", type(data_int))
print("data = ", data_float, "type = ", type(data_float))
print("data = ", data_bool, "type = ", type(data_bool))