# belajar casting
# merubah tipe dari dari satu tipe ke tipe lain
# tipe data : int, str, float, bool


print("====INTEGER====")
data_int = 2
data_bool2 = 0

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
data_bool3 = bool(data_bool2)

print("ini adalah : ", data_int, "dengan type : ", type(data_int))
print("ini adalah : ", data_float, "dengan type : ", type(data_float))
print("ini adalah : ", data_str, "dengan type : ", type(data_str))
print("ini adalah : ", data_bool, "dengan type : ", type(data_bool))

print("ini adalah : ", data_bool3, "dengan type : ", type(data_bool3))

# FLOAT
print("====FLOAT====")

data_float = 9.8

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("ini adalah data ", data_float, "dengan type : ", type(data_float))
print("ini adalah data ", data_int, "dengan type : ", type(data_int))
print("ini adalah data ", data_str, "dengan type : ", type(data_str))
print("ini adalah data ", data_bool, "dengan type : ", type(data_bool))

# BOOLEAN
print("====BOOLEAN====")

data_bool = True
data_bool = False

data_int = int(data_bool)
data_str = str(data_bool)
data_float = bool(data_bool)

print("ini adalah data ", data_float, "dengan type : ", type(data_float))
print("ini adalah data ", data_int, "dengan type : ", type(data_int))
print("ini adalah data ", data_str, "dengan type : ", type(data_str))
print("ini adalah data ", data_bool, "dengan type : ", type(data_bool))

# STRING
print("====STRING====")

data_str = "True" #ini kalo ke int dan float error karna bukan angka
data_str = "0" #ini int dan float aman karna angka tapi hasilnya di bool true bukan false
data_str = "1" #ini int dan float aman karna angka tapi hasilnya di bool true bukan false
data_str = "1.7"  #ini kalo ke int dan float error walaupun angka tapi tidak bisa menggunakan koma
data_str = "" # ini error karna str kosong tapi hasil bool nya false

data_int = int(data_str)
data_bool = str(data_str)
data_float = bool(data_str)

print("ini adalah data ", data_float, "dengan type : ", type(data_float))
print("ini adalah data ", data_int, "dengan type : ", type(data_int))
print("ini adalah data ", data_str, "dengan type : ", type(data_str))
print("ini adalah data ", data_bool, "dengan type : ", type(data_bool))