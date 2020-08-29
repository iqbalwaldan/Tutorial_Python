# nomer 1
# -------0+++++++5-------8+++++++11-------

inputuser = float(input("Masukkan angka :"))

# aturan 1
lebihdari0 = inputuser > 0
kurangdari5 = inputuser < 5
aturan1 = lebihdari0 and kurangdari5

# aturan 2
lebihdari8 = inputuser > 8
kurangdari11 = inputuser < 11
aturan2 = lebihdari8 and kurangdari11

# Penggabungan
aturan3 = aturan1 or aturan2
print(aturan3)

# nomer 2
# +++++++0-------5+++++++8-------11+++++++
inputuser = float(input("Masukkan angka :"))

# aturan 1
kurangdari0 = inputuser < 0
aturan1 = kurangdari0 

# aturan 2
lebihdari5 = inputuser > 5
kurangdari8 = inputuser < 8
aturan2 = lebihdari5 and kurangdari8

# aturan 3
lebihdari11 = inputuser > 11
aturan3 = lebihdari11

# penggabungan
aturan4 = aturan1 or aturan2 or aturan3
print(aturan4)

