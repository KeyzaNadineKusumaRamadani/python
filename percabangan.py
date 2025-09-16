# meminta pengguna memasukkan usia
usia = int(input("Masukkan usia anda:"))

# meentukan kategori usia
if 0<= usia <=13:
    print("kategori anak")
elif 14 <= usia <=24 :
    print("Kategori: remaja")
elif 25 <= usia <=49:
    print("kategori : Dewasa")
elif usia >=50:
    print("Kategori: lansia")
else:
    print("usia tidak valid")