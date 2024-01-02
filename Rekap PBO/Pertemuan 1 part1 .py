def main():
    print("+++++++++++++++++++++++++++++++++++++")
    print("")
    print("Selamat Datang di Pemilihan Presiden ")
    print("Berikut adalah Daftar  Calon Presiden ")
    print("1. Prabowo Subianto ")
    print("2. Joko Widodo ")
    print("3. Ganjar Pranowo ")
    print("")
    print("=====================================")
    
    pilihan =int(input("Masukkan Nomor Calon Presiden yang Anda Pilih "))

    if pilihan ==   1 :
        print("Anda Memilih Prabowo Subianto Sebagai Presiden ")
    elif pilihan == 2 :
        print("Anda Memilih Joko Widodo  Sebagai Presiden ")
    elif pilihan == 3 :
        print("Anda Memilih Ganjar Pranowo Sebagai Presiden ")
    else:
        ("Pilihan Anda Tidak Valid ")
main()