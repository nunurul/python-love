# Tipe data integer

data_integer = 1
print(type(data_integer))
print("ini adalah data : ", data_integer, " dengan tipe : ", type(data_integer))

# Tipe data float

data_float = 1.5
print(type(data_float))
print("ini adalah angaka : ", data_float, "dengan bertipe", type(data_float))

# Tipe data string

data_string = "hah"
print(type(data_string))
print("ini adalah : ", data_string, "dengan tipe data : ", type(data_string))

# Tipe data boolean

data_boolean = True
print(type(data_boolean))
print("ini adalah : ", data_boolean, "dengan tipe data : ", type(data_boolean))

# Tipe data khusus

# bilangan kompleks

data_complex = complex(5,6)
print(type(data_complex))
print("ini adalah : ", data_complex, "dengan tipe", type(data_complex)) 

# tipe data dari bahasa c

from ctypes import c_double

data_c_double = c_double(10.5)
print(type(data_c_double))
print("ini adalah ", data_c_double, "yang bertipe", type(data_c_double))