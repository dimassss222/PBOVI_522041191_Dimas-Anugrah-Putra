class Penghasilan:
    def __init__(self, jumlah_penghasilan):
        self.jumlah_penghasilan = jumlah_penghasilan

    def hitung_pajak(self):
        return self.jumlah_penghasilan * 0.1  # Misalnya, pajak 10% dari jumlah penghasilan


class Pajak(Penghasilan):
    def __init__(self, jumlah_penghasilan, jenis_pajak):
        super().__init__(jumlah_penghasilan)
        self.jenis_pajak = jenis_pajak

    def hitung_pajak(self):
        if self.jenis_pajak == "PPh21":
            return super().hitung_pajak() * 0.9  # Diskon 10% untuk PPh21
        else:
            return super().hitung_pajak()


# Membuat objek penghasilan
penghasilan1 = Penghasilan(5000000)
penghasilan2 = Penghasilan(1000000)

# Membuat objek pajak dengan jenis PPh21
pajak1 = Pajak(500000, "PPh21")
pajak2 = Pajak(100000, "PPh22")

# Menampilkan hasil perhitungan pajak
print("Penghasilan 1 - Pajak:", penghasilan1.hitung_pajak())
print("Penghasilan 2 - Pajak:", penghasilan2.hitung_pajak())
print("Pajak 1 - Pajak:", pajak1.hitung_pajak())
print("Pajak 2 - Pajak:", pajak2.hitung_pajak())
