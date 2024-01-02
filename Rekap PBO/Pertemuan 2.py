#Dimas Anugrah Putra Alfarizqy 
# # Studi Kasus
#3.5 - 4 = 6 MK
#3 - 3.49 = 4 MK
#2 - 2.99 = 3 MK
#1 - 1.99 = 2 MK
matakuliah = []

def menu():
    print("==========Menu Pengambilan Mata Kuliah ====================")
    print("1. Input Mata Kuliah")
    print("2. Lihat KRS")
    print("3. Keluar")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def tambah_matkul(mk):
    matakuliah.append(mk)
    print(f"{mk} Mata kuliah di tambah")

def Print_krs():
    print(" KRS anda : ")
    for mk in matakuliah:
        print("==================================")
        print("==================================")
        print("Mata Kuliah yang diambil :")
        print(f"- {mk}")

def matkul():
    print("==============================================")
    print("     Mata Kuliah yang tersedia")
    print("==============================================")
    print("   1. Pemrograman Beriorentasi Objek Praktik")
    print("   2. Agama Islam")
    print("   3. Sistem Operasi")
    print("   4. Kecerdasan Buatan")
    print("   5. Basis Data")
    print("   6. Pemrograman Web")
    print("   7. Sistem Digital")
    print("   8. Pengantar Analisis Data")
    print("   9. Pemrograman Web Praktik")
    print("  10. Coding Maching Learning ")
    print("  11. Aljabar Linear")

def main():
    nama = input("Masukkan Nama: ")
    npm = int(input("Masukkan NPM: "))
    ipk = float(input("Masukkan IPK: "))
    if   3.5 <= ipk <= 4.0:
        print("Anda Dapat Mengambil 6 Mata kuliah ")
    elif 3.0 <= ipk <= 3.49:
        print("Anda Dapat Mengambil 4 Mata Kuliah ")
    elif  2 <= ipk <= 2.99 :
        print("Anda Dapat Mengambil 3 Mata Kuliah   ")
    elif  0 <= ipk <= 1.99 :
        print("Anda Dapat Mengambil 2 Mata Kuliah ")
    else:
        print("Anda ")
    matkul()

    if 3.5 <= ipk <= 4.0:
        perulangan = 1
        while perulangan <= 6:
            mata_kuliah = input("Masukkan Mata kuliah: ")
            tambah_matkul(mata_kuliah)
            perulangan += 1

    elif 3.0 <= ipk < 3.5:
        perulangan = 1
        while perulangan <= 4:
            mata_kuliah = input("Masukkan Mata kuliah: ")
            tambah_matkul(mata_kuliah)
            perulangan += 1

    elif 2 <= ipk < 3.0:
        perulangan = 1
        while perulangan <= 3:
            mata_kuliah = input("Masukkan Mata kuliah: ")
            tambah_matkul(mata_kuliah)
            perulangan += 1
    elif 0 <= ipk < 2:
        perulangan = 1
        while perulangan <= 2:
            mata_kuliah = input("Masukkan Mata kuliah: ")
            tambah_matkul(mata_kuliah)
            perulangan += 1
    else:
        print("Input IPK tidak valid")

while True:
    menu()
    pilihan = int(input("Pilih opsi: "))

    if pilihan == 1:
        main()
    elif pilihan == 2:
        Print_krs()
    elif pilihan == 3:
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")