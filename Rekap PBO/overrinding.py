class pajak():
    def __init__(self, nominal, lama):
        self.nominal : nominal
        self.lama    : lama 
    def jumlah(self):
        print(" Total Pajak yang harus anda bayar : ",self.nominal * self.lama, )

class penghasilan(pajak):
    def __init__(self, gaji,lamakerja):
        self.gaji=gaji
        self.lamakerja= lamakerja
        pajak.__init__(self,nominal,lama)
    def jumlah(self):
        print("Total Penghasilan = ", self.gaji * self.lamakerja)

p=pajak (500000,10)
p2=penghasilan(6500000,10)
p.jumlah()
p2.jumlah()


