#DimasAnugrah Putra Alfarizqy
#5220411191

class Karyawan:
    def __init__(self, nama, jabatan, gaji=0):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    def tampilkan_gaji_fulltime(self):
        print(f'Nama Karyawan: {self.nama}')
        print(f'Jabatan Karyawan: {self.jabatan}')
        print(f'Gaji Karyawan: {self.gaji}')

    def tampilkan_gaji_parttime(self):
        print(f'Nama Karyawan: {self.nama}')
        print(f'Jabatan Karyawan: {self.jabatan}')
        print(f'Gaji Karyawan: {self.gaji}')

class KaryawanFulltime(Karyawan):
    def __init__(self, nama, jabatan,jam_kerja_fulltime):
        super().__init__(nama, jabatan)
        self.gaji = 600000* jam_kerja_fulltime
    def hitung_gaji_
class KaryawanParttime(Karyawan):
    def __init__(self, nama, jabatan, jam_kerja, jam_lembur=0):
        super().__init__(nama, jabatan)
        self.gaji_perjam = 15000
        self.jam_kerja = jam_kerja
        self.jam_lembur = jam_lembur

    def hitung_gaji(self):
        gaji_pokok = self.jam_kerja * self.gaji_perjam
        total_jam_kerja = self.jam_kerja + self.jam_lembur
        if total_jam_kerja > 40:
            print("Jumlah jam kerja maksimum 40 jam")
            return 0
        lembur = self.hitung_lembur(self.jam_lembur)
        total_gaji = gaji_pokok + lembur
        return total_gaji

    def hitung_lembur(self, jam_lembur):
        tarif_lembur = 10000
        return jam_lembur * tarif_lembur

# Menu 
def menu_karyawan():
    while True:
        print("===== \nMenu Karyawan:======")
        print("===== 1. Tampilkan Informasi Karyawan Full-time ====")
        print("===== 2. Tampilkan Informasi Karyawan Part-time ====")
        print("===== 3. Keluar =====" )

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            jam_kerja_fulltime = int(input('Masukkan Jumlah Bulan kerja : '))
            karyawan_fulltime = KaryawanFulltime("Agus Ahmad", "HRD",jam_kerja_fulltime)
            karyawan_fulltime.tampilkan_gaji_fulltime()
        elif pilihan == "2":
            jam_kerja = int(input("Masukkan jumlah jam kerja: "))
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            karyawan_parttime = KaryawanParttime("Toni Syah", "Office Boy", jam_kerja, jam_lembur)
            gaji_total = karyawan_parttime.hitung_gaji()
            print(f'Total Gaji Karyawan Part-time: {gaji_total}')
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu_karyawan()
