class bidang :
    def __init__ (self, x, y, z):
        self.xx =x
        self.yy= y
        self.zz= z 
    def hitungLuas (self):
        luas = self.xx * self.yy * self.zz
        return luas 
    def bintang():
        print("*"*15)
    
bidang.bintang()
sisi = int(input("Masukkan Sisi/Lebar  = "))
panjang = int(input("Masukkan Panjang  = "))
jari    = int(input("Masukkan Jari Jari = "))
bidang.bintang()

persegi= bidang(sisi,sisi,1)
persegipanjang = bidang(panjang,sisi,1)
segitiga = bidang(panjang,sisi,0.5)
lingkaran = bidang (jari,jari,3.14)

print("Luas Persegi ", persegi.hitungLuas())
print("Luas Persegipanjang ", persegipanjang.hitungLuas())
print("Luas Segitiga : ", segitiga.hitungLuas())
print("Luas Lingkaran : ", lingkaran.hitungLuas())