from datetime import datetime, timedelta

class Kamera:
    def __init__(self, tipe_kamera, tarif_harian):
        self.tipe_kamera = tipe_kamera
        self.tarif_harian = tarif_harian

    def hitung_biaya_sewa(self, hari):
        total_biaya = self.tarif_harian * hari
        if hari > 7:
            total_biaya *= 0.7  # Diskon 30% untuk sewa lebih dari 7 hari
        return total_biaya

    def tampilkan_info(self, tanggal_mulai, tanggal_selesai):
        print(f"{self.tipe_kamera} - Tarif Harian: {self.tarif_harian:,}")
        print(f"   Periode Sewa: {tanggal_mulai.strftime('%Y-%m-%d')} sampai {tanggal_selesai.strftime('%Y-%m-%d')}")


class DSLR(Kamera):
    def __init__(self, hari_sewa):
        super().__init__("DSLR", 200000)
        self.hari_sewa = hari_sewa

    def hitung_biaya_sewa(self):
        return super().hitung_biaya_sewa(self.hari_sewa)

    def tampilkan_info(self, tanggal_mulai):
        tanggal_selesai = tanggal_mulai + timedelta(days=self.hari_sewa)
        super().tampilkan_info(tanggal_mulai, tanggal_selesai)


class Mirrorless(Kamera):
    def __init__(self, hari_sewa):
        super().__init__("Mirrorless", 300000)
        self.hari_sewa = hari_sewa

    def hitung_biaya_sewa(self):
        return super().hitung_biaya_sewa(self.hari_sewa)

    def tampilkan_info(self, tanggal_mulai):
        tanggal_selesai = tanggal_mulai + timedelta(days=self.hari_sewa)
        super().tampilkan_info(tanggal_mulai, tanggal_selesai)


class ActionCam(Kamera):
    def __init__(self, hari_sewa):
        super().__init__("Action Cam", 350000)
        self.hari_sewa = hari_sewa

    def hitung_biaya_sewa(self):
        return super().hitung_biaya_sewa(self.hari_sewa)

    def tampilkan_info(self, tanggal_mulai):
        tanggal_selesai = tanggal_mulai + timedelta(days=self.hari_sewa)
        super().tampilkan_info(tanggal_mulai, tanggal_selesai)


class Sewa:
    def __init__(self):
        self.kamera = []
        self.hari_sewa = None

    def tambah_kamera(self, kamera):
        self.kamera.append(kamera)

    def atur_durasi_sewa(self, hari_sewa):
        self.hari_sewa = hari_sewa

    def hitung_total_biaya(self):
        total_biaya = sum(kamera.hitung_biaya_sewa() for kamera in self.kamera)
        return total_biaya

    def tampilkan_detail_sewa(self):
        print("\nDetail Sewa:")
        for kamera in self.kamera:
            tanggal_mulai = datetime.now()
            kamera.tampilkan_info(tanggal_mulai)


def tampilkan_submenu():
    print("1. Pilih Tipe Kamera")
    print("2. Tampilkan Detail Sewa")
    print("3. Kembali ke Menu Utama")


def dapatkan_durasi_sewa():
    hari = int(input("Masukkan jumlah hari sewa: "))
    return hari


def main():
    penyewaan = Sewa()

    while True:
        print("\n========= Selamat Datang di SKY PHOTOGRAPHY =========== ")
        print("==========================================================")
        print("============ Pilih Menu yang Anda Inginkan ===============")
        print("============= 1. Sewa Kamera =============================")
        print("============= 2. Pembayaran ==============================")
        print("============= 3. Keluar ==================================")

        pilihan = input("Masukkan Menu yang Anda Pilih : ")

        if pilihan == "1":
            while True:
                tampilkan_submenu()
                pilihan_submenu = input("Masukkan Pilihan Anda : ")

                if pilihan_submenu == "1":
                    print("====== Pilih tipe kamera yang akan disewa ==========")
                    print("====== 1. DSLR       =======")
                    print("====== 2. Mirrorless =======")
                    print("====== 3. Action Cam =======")

                    pilihan_kamera = input("Masukkan Tipe Kamera yang Anda Ingin Sewa: ")

                    if pilihan_kamera == "1":
                        penyewaan.tambah_kamera(DSLR(dapatkan_durasi_sewa()))
                    elif pilihan_kamera == "2":
                        penyewaan.tambah_kamera(Mirrorless(dapatkan_durasi_sewa()))
                    elif pilihan_kamera == "3":
                        penyewaan.tambah_kamera(ActionCam(dapatkan_durasi_sewa()))
                    else:
                        print("Pilihan kamera tidak valid. Coba lagi.")

                elif pilihan_submenu == "2":
                    print("============================")

                    penyewaan.tampilkan_detail_sewa()

                    print("============================")

                elif pilihan_submenu == "3":
                    break

                else:
                    print("Pilihan tidak valid. Coba lagi.")

        elif pilihan == "2":
            total_biaya = penyewaan.hitung_total_biaya()
            penyewaan.tampilkan_detail_sewa()
            print(f"\nTotal biaya sewa untuk semua kamera: {total_biaya:,.2f}")

        elif pilihan == "3":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
