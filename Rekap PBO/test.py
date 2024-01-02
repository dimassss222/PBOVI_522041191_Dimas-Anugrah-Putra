class Buku:
    def __init__(self, judul, pengarang, jumlah_halaman):
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah_halaman = jumlah_halaman
        self.tersedia = True

    def informasi_buku(self):
        return f"Judul: {self.judul}, Pengarang: {self.pengarang}, Jumlah Halaman: {self.jumlah_halaman}"

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return f"Buku '{self.judul}' berhasil dipinjam."
        else:
            return f"Maaf, buku '{self.judul}' sedang tidak tersedia."

    def kembalikan(self):
        if not self.tersedia:
            self.tersedia = True
            return f"Buku '{self.judul}' berhasil dikembalikan."
        else:
            return f"Buku '{self.judul}' sudah tersedia."


class AnggotaPerpustakaan:
    def __init__(self, nama, nomor_anggota):
        self.nama = nama
        self.nomor_anggota = nomor_anggota

    def informasi_anggota(self):
        return f"Nama: {self.nama}, Nomor Anggota: {self.nomor_anggota}"

    def pinjam_buku(self, buku):
        return f"{self.nama} {buku.pinjam()}"

    def kembalikan_buku(self, buku):
        return f"{self.nama} {buku.kembalikan()}"


class Perpustakaan:
    def __init__(self, nama_perpustakaan, lokasi):
        self.nama_perpustakaan = nama_perpustakaan
        self.lokasi = lokasi
        self.daftar_buku = []
    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
    def informasi_perpustakaan(self):
        return f"Perpustakaan: {self.nama_perpustakaan}, Lokasi: {self.lokasi},Judul Buku yang Tersedia : {len(self.daftar_buku)}"


# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu:")
    print("1. Informasi Perpustakaan")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Tambah Buku")
    print("0. Keluar")


Perpustakaan = Perpustakaan("Perpustakaan SDA MINERAL","Jalan Imam Bonjol no.13 Kabupaten Bekasi ")

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan : ")

    if pilihan == "1":
        print(Perpustakaan.informasi_perpustakaan())
    elif pilihan == "2":
        nama_peminjam = input("Masukkan nama peminjam: ")
        nomor_anggota = input("Masukkan nomor anggota: ")
        nama_buku = input("Masukkan nama buku yang ingin dipinjam: ")

        buku_terpilih = None
        for buku in Perpustakaan.daftar_buku:
            if buku.judul == nama_buku:
                buku_terpilih = buku
                break

        if buku_terpilih:
            anggota = AnggotaPerpustakaan(nama_peminjam, nomor_anggota)
            print(anggota.pinjam_buku(buku_terpilih))
        else:
            print(f"Buku dengan nama '{nama_buku}' tidak ditemukan.")

    elif pilihan == "3":
        nama_peminjam = input("Masukkan nama peminjam: ")
        nama_buku = input("Masukkan nama buku yang ingin dikembalikan: ")

        buku_terpilih = None
        for buku in perpustakaan.daftar_buku:
            if buku.judul == nama_buku:
                buku_terpilih = buku
                break

        if buku_terpilih:
            anggota = AnggotaPerpustakaan(nama_peminjam, "")
            print(anggota.kembalikan_buku(buku_terpilih))
        else:
            print(f"Buku dengan nama '{nama_buku}' tidak ditemukan.")

    elif pilihan == "4":
        judul_buku = input("Masukkan judul buku: ") 
        pengarang_buku = input("Masukkan pengarang buku: ") 
        halaman_buku = int(input("Masukkan jumlah halaman buku: ")) 
        buku_baru = Buku(judul_buku, pengarang_buku, halaman_buku) 
        Perpustakaan.tambah_buku(buku_baru) 
        print(f"Buku '{judul_buku}' berhasil ditambahkan.") 
    elif pilihan == "0": 
        print("Terima kasih. Keluar dari program.") 
        break 
    else: 
        print("Pilihan tidak valid. Silakan coba lagi.")