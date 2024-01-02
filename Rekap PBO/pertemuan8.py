class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahun_terbit = tahun_terbit
        self.__tersedia = True  # 

    def informasi_buku(self):
        return f"Judul: {self.__judul}, Pengarang: {self.__pengarang}, Tahun Terbit: {self.__tahun_terbit}"

    def pinjam_buku(self):
        if self.__tersedia:
            self.__tersedia = False
            return "Buku berhasil dipinjam."
        else:
            return "Maaf, buku sedang tidak tersedia."

    def kembalikan_buku(self):
        if not self.__tersedia:
            self.__tersedia = True
            return "Buku berhasil dikembalikan."
        else:
            return "Buku sudah tersedia."


class AnggotaPerpustakaan:
    def __init__(self, nama, nomor_anggota):
        self.__nama = nama
        self.__nomor_anggota = nomor_anggota

    def informasi_anggota(self):
        return f"Nama: {self.__nama}, Nomor Anggota: {self.__nomor_anggota}"

    def pinjam_buku(self, buku):
        return f"{self.__nama} {buku.pinjam_buku()}"

    def kembalikan_buku(self, buku):
        return f"{self.__nama} {buku.kembalikan_buku()}"


class Perpustakaan:
    def __init__(self, nama_perpustakaan, lokasi):
        self.__nama_perpustakaan = nama_perpustakaan
        self.__lokasi = lokasi
        self.__daftar_buku = []

    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)

    def informasi_perpustakaan(self):
        return f"Perpustakaan: {self.__nama_perpustakaan}, Lokasi: {self.__lokasi}"

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu:")
    print("1. Informasi Perpustakaan")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("0. Keluar")

# Contoh Penggunaan
buku1 = Buku("Harry Potter", "J.K. Rowling", 2001)
buku2 = Buku("Sherlock Holmes", "Arthur Conan Doyle", 1892)

anggota1 = AnggotaPerpustakaan("Alice", "A001")

perpustakaan = Perpustakaan("Perpustakaan Kota", "Jl. Pustaka No. 123")
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print(perpustakaan.informasi_perpustakaan())
    elif pilihan == "2":
        print(anggota1.pinjam_buku(buku1))
    elif pilihan == "3":
        print(anggota1.kembalikan_buku(buku1))
    elif pilihan == "0":
        print("Terima kasih. Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")