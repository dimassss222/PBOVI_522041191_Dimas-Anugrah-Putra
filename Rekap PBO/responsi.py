#DimasAnugrah Putra Alfarizqy
#5220411191

class Karyawan:
    def __init__(self, nama, jabatan, gaji=0):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    def tampilkan_informasi(self):
        print(f'Nama Karyawan: {self.nama}')
        print(f'Jabatan Karyawan: {self.jabatan}')

class KaryawanFulltime(Karyawan):
    def __init__(self, nama, jabatan, jam_kerja_fulltime):
        super().__init__(nama, jabatan)
        self.gaji = 600000 * jam_kerja_fulltime

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print(f'Total Gaji Karyawan full time : {self.gaji}')




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
            lembur = self.hitung_lembur(total_jam_kerja - 40)
            total_gaji = gaji_pokok + lembur
        else:
            total_gaji = gaji_pokok
        return total_gaji

    def hitung_lembur(self, jam_lembur):
        tarif_lembur = 10000
        return jam_lembur * tarif_lembur

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        total_gaji = self.hitung_gaji()
        print(f'Total Gaji Karyawan Part-time: {total_gaji}')


# Menu
def menu_karyawan():
    while True:
        print("===== \nMenu Karyawan:======")
        print("===== 1. Tampilkan Informasi Karyawan Full-time ====")
        print("===== 2. Tampilkan Informasi Karyawan Part-time ====")
        print("===== 3. Keluar =====")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            jam_kerja_fulltime = int(input('Masukkan Jumlah Bulan kerja : '))
            karyawan_fulltime = KaryawanFulltime("Agus Ahmad", "HRD", jam_kerja_fulltime)
            karyawan_fulltime.tampilkan_informasi()
        elif pilihan == "2":
            jam_kerja = int(input("Masukkan jumlah jam kerja: "))
            jam_lembur = int(input("Masukkan jumlah jam lembur: "))
            karyawan_parttime = KaryawanParttime("Toni Syah", "Office Boy", jam_kerja, jam_lembur)
            karyawan_parttime.tampilkan_informasi()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    menu_karyawan()
