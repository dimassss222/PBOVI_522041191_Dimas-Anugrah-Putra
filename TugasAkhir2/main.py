import mysql.connector
from os import system, name
from tabulate import tabulate


def clear_terminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

if mydb.is_connected():
    print("Berhasil terhubung ke database")
else:
    print("Gagal terhubung ke database")
    quit()


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS perangkat "
                 + "(kode_barang INT PRIMARY KEY, "
                 + "nama VARCHAR(255), "
                 + "harga VARCHAR(255))")

mycursor.execute("CREATE TABLE IF NOT EXISTS komputer "
                 + "(kode_barang INT PRIMARY KEY, "
                 + "nama VARCHAR(255), "
                 + "harga VARCHAR(255), "
                 + "ram VARCHAR(255), "
                 + "processor VARCHAR(255), "
                 + "harddisk VARCHAR(255))")

class Perangkat:
    def __init__(self, kode_barang=None, nama=None, harga=None):
        self.kode_barang = kode_barang
        self.nama = nama
        self.harga = harga

    def tambah(self):
        sql = "INSERT INTO perangkat (kode_barang, nama, harga) VALUES (%s, %s, %s)"
        val = (self.kode_barang, self.nama, self.harga)
        mycursor.execute(sql, val)
        mydb.commit()
        print("data berhasil ditambahkan")

    def tampil(self):
        sql = "SELECT * FROM perangkat"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        print(tabulate(results, headers=['Kode', 'Nama', 'Harga'], tablefmt='psql'))

    def update(self):
        sql = "UPDATE perangkat SET nama = %s, harga = %s WHERE kode_barang = %s"
        val = (self.nama, self.harga, self.kode_barang)
        mycursor.execute(sql, val)
        mydb.commit()
        print("data berhasil diubah")

    def hapus(self):
        sql = "DELETE FROM perangkat WHERE kode_barang = %s"
        val = (self.kode_barang,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("data berhasil dihapus")


class Komputer(Perangkat):
    def __init__(self, kode_barang=None, nama=None, harga=None, ram=None, processor=None, harddisk=None):
        super().__init__(kode_barang, nama, harga)
        self.ram = ram
        self.processor = processor
        self.harddisk = harddisk

    def tambah(self):
        sql = "INSERT INTO komputer (kode_barang, nama, harga, ram, processor, harddisk) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.kode_barang, self.nama, self.harga, self.ram, self.processor, self.harddisk)
        mycursor.execute(sql, val)
        mydb.commit()
        print("data berhasil ditambahkan")

    def tampil(self):
        sql = "SELECT * FROM komputer"
        mycursor.execute(sql)
        results = mycursor.fetchall()
        print(tabulate(results, headers=['Kode', 'Nama', 'Harga', 'RAM', 'Processor', 'Harddisk'], tablefmt='psql'))

    def update(self):
        sql = "UPDATE komputer SET nama = %s, harga = %s, ram = %s, processor = %s, harddisk = %s WHERE kode_barang = %s"
        val = (self.nama, self.harga, self.ram, self.processor, self.harddisk, self.kode_barang)
        mycursor.execute(sql, val)
        mydb.commit()
        print("data berhasil diubah")

    def hapus(self):
        sql = "DELETE FROM komputer WHERE kode_barang = %s"
        val = (self.kode_barang,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("data berhasil dihapus")

def menu_perangkat():
    clear_terminal()
    print("=== Manajemen Perangkat ===")
    print("1. Tambah Data Perangkat")
    print("2. Lihat Data Perangkat")
    print("3. Update Data Perangkat")
    print("4. Hapus Data Perangkat")
    print("5. Keluar")
    menu = input("Pilih menu> ")

    if menu == "1":
        clear_terminal()
        kode_barang = input("Kode Barang: ")
        nama = input("Nama: ")
        harga = input("Harga: ")
        perangkat = Perangkat(kode_barang, nama, harga)
        perangkat.tambah()
        input("Tekan ENTER untuk kembali ke MENU")

    elif menu == "2":
        clear_terminal()
        perangkat = Perangkat()
        perangkat.tampil()
        input("Tekan ENTER untuk kembali ke MENU")

    elif menu == "3":
        clear_terminal()
        perangkat = Perangkat()
        perangkat.tampil()

        kode_barang = input("Kode Barang: ")
        nama = input("Nama: ")
        harga = input("Harga: ")
        perangkat = Perangkat(kode_barang, nama, harga)
        perangkat.update()
        input("Tekan ENTER untuk kembali ke MENU")


    elif menu == "4":
        clear_terminal()
        perangkat = Perangkat()
        perangkat.tampil()

        kode_barang = input("Kode Barang: ")
        Perangkat(kode_barang).hapus()
        input("Tekan ENTER untuk kembali ke MENU")

def menu_komputer():
    clear_terminal()
    print("=== Manajemen Komputer ===")
    print("1. Tambah Data Komputer")
    print("2. Lihat Data Komputer")
    print("3. Update Data Komputer")
    print("4. Hapus Data Komputer")
    print("5. Keluar")
    menu = input("Pilih menu> ")

    if menu == "1":
        clear_terminal()
        kode_barang = input("Kode Barang: ")
        nama = input("Nama: ")
        harga = input("Harga: ")
        ram = input("RAM: ")
        processor = input("Processor: ")
        harddisk = input("Harddisk: ")
        komputer = Komputer(kode_barang, nama, harga, ram, processor, harddisk)
        komputer.tambah()

    elif menu == "2":
        clear_terminal()
        komputer = Komputer()
        komputer.tampil()
        input("Tekan ENTER untuk kembali ke MENU")

    elif menu == "3":
        clear_terminal()
        komputer = Komputer()
        komputer.tampil()

        kode_barang = input("Kode Barang: ")
        nama = input("Nama: ")
        harga = input("Harga: ")
        ram = input("RAM: ")
        processor = input("Processor: ")
        harddisk = input("Harddisk: ")
        komputer = Komputer(kode_barang, nama, harga, ram, processor, harddisk)
        komputer.update()
        input("Tekan ENTER untuk kembali ke MENU")

    elif menu == "4":
        clear_terminal()
        komputer = Komputer()
        komputer.tampil()

        kode_barang = input("Kode Barang: ")
        Komputer(kode_barang).hapus()
        input("Tekan ENTER untuk kembali ke MENU")

# Main Program
while True:
    clear_terminal()
    print("=== Menu Utama ===")
    print("1. Perangkat")
    print("2. Komputer")
    print("3. Keluar")

    menu = input("Pilih menu> ")

    if menu == "1":
        menu_perangkat()
    elif menu == "2":
        menu_komputer()
    elif menu == "3":
        print("Program selesai, sampai jumpa!")
        break

        

    



