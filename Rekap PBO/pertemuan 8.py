class Katalog:
    def cari(self, keyword):
        self.keyword = keyword


class Perpustakaan(Katalog):
    def __init__(self, judul, subjek):
        super().__init__()  
        self.judul = judul
        self.subjek = subjek
        self.rak = {'a': [], 'b': [], 'c': [], 'd': []}

    def lokasi_penyimpanan(self):
        return self.rak

    def info(self):
        return f"Perpustakaan: {self.nama}, Subjek: {self.subjek}"

class DVD(Katalog):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__()
        self.judul = judul
        self.subjek = subjek
        self.aktor = aktor
        self.genre = genre


class Majalah(Katalog):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__()  
        self.judul = judul
        self.subjek = subjek
        self.volume = volume
        self.issue = issue


class Buku(Katalog):
    def __init__(self, judul, subjek, isbn, pengarang, jumlah_halaman, ukuran):
        super().__init__()  
        self.judul = judul
        self.subjek = subjek
        self.isbn = isbn
        self.pengarang = pengarang
        self.jumlah_halaman = jumlah_halaman
        self.ukuran = ukuran


class Pengarang(Buku):
    def __init__(self, nama, isbn, pengarang, jumlah_halaman, ukuran):
        super().__init__(nama, isbn, pengarang, jumlah_halaman, ukuran) 
        self.nama = nama
    def info(self):
        return f"Pengarang: {self.nama}, ISBN: {self.isbn}, Jumlah Halaman: {self.jumlah_halaman}, Ukuran: {self.ukuran}"
    def cari(self, keyword):
        if keyword.lower() in self.nama.lower():
            return f"Buku oleh pengarang {self.nama} ditemukan."
        else:
            return f"Tidak ada buku oleh pengarang {self.nama} dengan kata kunci '{keyword}'."



def tampilkan_menu():
    print("Menu:")
    print("1. Cari Katalog")
    print("2. Lokasi Penyimpanan Perpustakaan")
    print("3. Info Perpustakaan")
    print("4. Tambah DVD")
    print("5. Tambah Majalah")
    print("6. Tambah Buku")
    print("7. Info Pengarang")
    print("8. Cari Pengarang")
    print("0. Keluar")



Perpustakaan = Perpustakaan("Perpustakaan Kota", "Umum")

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan = ")
    if pilihan == "1":
        keyword = input("Masukkan kata kunci: ")
        Perpustakaan.cari(keyword)
    elif pilihan == "2":
        Perpustakaan.lokasi_penyimpanan()
    elif pilihan == "3":
        Perpustakaan.info()
    elif pilihan == "4":
        judul = input("Masukkan judul DVD: ")
        subjek = input("Masukkan subjek DVD: ")
        aktor = input("Masukkan nama aktor: ")
        genre = input("Masukkan genre DVD: ")
        dvd = DVD(judul, subjek, aktor, genre)
    elif pilihan == "5":
        judul = input("Masukkan judul majalah: ")
        subjek = input("Masukkan subjek majalah: ")
        volume = input("Masukkan volume majalah: ")
        issue = input("Masukkan issue majalah: ")
        majalah = Majalah(judul, subjek, volume, issue)
    elif pilihan == "6":
        judul = input("Masukkan judul buku: ")
        subjek = input("Masukkan subjek buku: ")
        isbn = input("Masukkan ISBN buku: ")
        Pengarang = input("Masukkan nama pengarang buku: ")
        jumlah_halaman = input("Masukkan jumlah halaman buku: ")
        ukuran = input("Masukkan ukuran buku: ")
        buku = Buku(judul, subjek, isbn, Pengarang, jumlah_halaman, ukuran)
    elif pilihan == "7":
        nama_pengarang = input("Masukkan nama pengarang: ")
        isbn = input("Masukkan ISBN karya pengarang: ")
        jumlah_halaman = input("Masukkan jumlah halaman karya pengarang: ")
        ukuran = input("Masukkan ukuran karya pengarang: ")
        Pengarang = Pengarang(nama_pengarang, isbn, nama_Pengarang, jumlah_halaman, ukuran)
    elif pilihan == "8":
        keyword_pengarang = input("Masukkan kata kunci pengarang: ")
        Pengarang.cari(keyword_Pengarang)
    elif pilihan == "0":
        print("Terima kasih. Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
