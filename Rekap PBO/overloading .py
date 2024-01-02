class KlubBola:
    jumlah = 0 
    def __init__(self, pemain, bonus):
        self.pemain = pemain 
        self.bonus  = bonus
        KlubBola.jumlah += 1

    def tampilJumlah(self):
        print(" Total Pemain yang Mendapat Bonus : ", KlubBola.jumlah)
    
    def tampilPemain(self):
        print("Nama : ",self.pemain, " Bonus = ",self.bonus)
        
        #Overloading 

    def asuransi (self, cedera=None, perawatan=None):
        if cedera != None and perawatan != None:
            total = cedera + perawatan
            print("Asuransi Cedera + Perawatan = ",total)
        else:
            total= cedera
            print("Asuransi Cedera   = ",total)
        
        #Callling 

pemain1= KlubBola("Evan Dimas ", 7500000)
pemain2= KlubBola("Ryan Giggs", 9000000)
pemain3= KlubBola("Witan Sulaeman ", 7500000)
pemain1.tampilPemain()
pemain2.tampilPemain()
pemain3.tampilPemain()

pemain1.asuransi(5000000,3500000)
pemain2.asuransi(9000000,)
pemain3.asuransi(1000000,5000000)

print("Total Pemain %d"% KlubBola.jumlah)
rataBonus= (pemain1.bonus + pemain2.bonus + pemain3.bonus)/KlubBola.jumlah
print("Rata - Rata Bonus = "+str(rataBonus))


