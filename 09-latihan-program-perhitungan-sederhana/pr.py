# konfersi dari fahrenheit ke kelvin

fahrenheit = float(input("masukkan suhu fahrenheit :"))
celcius = (fahrenheit - 32) * (5/9)
kelvin = celcius + 273 
print ('suhu dalam kelvin adalah', kelvin)

# komfersi dari kelvin ke fahrenheit

kelvin = float(input('masukkan suhu kelvin :'))
celcius = kelvin - 273
fahrenheit = ((9/5)*celcius) + 32
print ('suhu dalam fahrenheit adalah', fahrenheit)