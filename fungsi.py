import math

# membuat fungsi unutk menghitung luas dan keliling lingkaran
def hitung_lingkaran(jari_jari):
    luas= math.pi *(jari_jari**2)
    keliling = 2 * math.pi * jari_jari
    return luas, keliling

# memanggil fungsi dan menampilkan hasil
jari = float(input("Masukkan jari-jari lingkaran:"))
luas, keliling = hitung_lingkaran(jari)

print(f"luas lingkaran = {luas:2f}" )
print(f"keliling lingkaran = {keliling:.2f}")