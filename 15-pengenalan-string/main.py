data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat sring 

'''
    1. dengan menggunakan single quote '..'
    2. dengan menggunakan double quote ".."
'''

data = 'menggunakan sigel quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar"')
print("'Halo, apa kabar'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\t\t\totong, semakin jauh")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3. String literal atau RAW

# hati-hati
print('c:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
""")

