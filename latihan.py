print("hallo")
print ("hallo semua")

# integer
contoh_list = [1,2,3,4,5,6]
print(contoh_list)
contoh_list_kedua =["a","b","c","d","e"]
print(contoh_list_kedua)
a=3
a= a+4
print(a)
#  dictionary
daftar_harga = {"apel" :5000,"jeruk" :8500,"mangga" : 7800, "duku" : 6500}
print (daftar_harga["mangga"])
print(daftar_harga.keys())
print(daftar_harga.values())

# printing
1+2
2+3
3+4
print(1+2)
print(2+3)
print(3+4)

# contoh untuk simpan sekaligus print nilai
def luas_keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang * lebar)
    return luas, keliling

luas_keliling(10,5)
luas_keliling(10,5)[0]
jwb_luas, jwb_keliling = luas_keliling(7,4)
print(jwb_keliling)
print(jwb_luas)

def luas_keliling(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    
    print("luas persegi panjang :" , luas)
    print("keliling persegi panjang:", keliling)
    luas_keliling(9,5)
    return luas, keliling