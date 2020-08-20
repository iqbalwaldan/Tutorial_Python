# Operasi Aritmatika

a = 10
b = 3

# Operasi Penjumlahan +
hasil = a + b
print(a," + ",b," = ", hasil)

# Operasi Pengurangan -
hasil = a - b
print(a," - ",b," = ", hasil)

# Operasi Perkalian *
hasil = a * b
print(a," * ",b," = ", hasil)

# Operasi Pembagian /
hasil = a / b
print(a," / ",b," = ", hasil)

# Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a," ** ",b," = ", hasil)

# Operasi Modulus %
hasil = a % b
print(a," % ",b," = ", hasil)

# Operasi Floor devision //
hasil = a // b
print(a," // ",b," = ", hasil)

# Prioritas operasi, Operational precedence
""" Urutannya adalah: () => Exponen => Perkalian/pembagian/modulus/floor => penjumlahan dan pengurangan """

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, " = ", hasil)
# kurung dikerjakan duluan
hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, '=', hasil)