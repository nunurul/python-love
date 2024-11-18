# Opperasi Aritmatika

a = 10
b = 8

# operasi penjumlahan (+)

hasil = a + b
print(a,"+",b,"=",hasil)

# operasi pengurangan (-)

hasil = a - b
print(a,"-",b,"=",hasil)

# operasi perkalian (*)

hasil = a * b
print(a,"*",b,"=",hasil)

# operasi pembagian (/)

hasil = a / b
print(a,"/",b,"=",hasil)

# operasi eksponen atau perpangkatan (**)

hasil = a ** b
print(a,"**",b,"=",hasil)

# operasi modulus (%)

hasil = a % b
print(a,"%",b,"=",hasil)

# operasi floor division (//)

hasil = a // b
print(a,"//",b,"=",hasil)

# operasi prioritas, operational precedence

x = 3
y = 2
z = 4

hasil = x ** y *z + x / y - y % z // x
print( x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=",hasil)

# kurung akan mengambil langkah pertama

r = 5
s = 6
t = 4

# before

hasil = r + s * t
print(hasil)

# after

hasil = (r + s) * t
print(hasil)