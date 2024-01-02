class Layanan :
    def __init__(self,nama,jenis,harga):
        self.nama = nama
        self.jenis= jenis
        self.harga= harga

def menu_layanan():
    print("====================================")
    print("        MENU LAYANAN NASABAH        ")
    print("====================================")
    print("1. Layanan  Deposito  ")
    print("2. Layanan  Giro      ")
    print("3. Layanan  Transfer  ")
    print("4. Layanan  Tabungan  ")
    print("5. Layanan  Kredit    ")

def main():
    nama_nasabah=input("Masukkan Nama Nasabah :  ")
    penghasilan =int(input("Masukkan Jumlah Penghasilan Anda(dalam Juta): ")) 

    if  penghasilan >500 :
        print("Anda Dapat Memilih Maximal 3 Layanan ")
        max_layanan = 3
    elif 100<= penghasilan <=499:
        print("Anda Dapat Memilih Maximal 2 Layanan ")
        max_layanan = 2
    elif penghasilan <=99:
        print("Anda Dapat Memilih Maximal 1 Layanan ")
        max_layanan = 1 
    else:
        print("Input Penghasilan  Tidak Valid ")
        return

    layanan_terpilih = []

    for k in range(max_layanan):
        menu_layanan()
        pilihan= int(input("Masukkan Pilihan Anda  : "))
    
    if 1 <= pilihan <=5 and pilihan not in layanan_terpilih:
        layanan_terpilih.append(pilihan)
    else:
        print("Pilihan Anda Tidak Valid atau Sudah Dipilih ,, Silahkan Coba Lagi")
    
    print("\n Layanan Yang Dipilih : ")
    total_pembayaran =0

    for i ,layanan_index in enumerate(layanan_terpilih, 1 ):
        lama_layanan=str(input("Masukkan Lama Layanan Untuk {layanan_list[layanan_index - 1].nama} = "))
        layanan = Layanan(layanan_list[layanan_index - 1].nama,layanan_list[layanan_index -1].jenis, layanan_list[layanan_index - 1 ].harga,)
        print(f"{i}.{layanan.nama} - {layanan_jenis} - Lama : {layanan.lama} - Harga : {layanan.harga} Juta ")
        total_pembayaran += layanan.harga
    
    print(f"\n Total Pembayaran : {total_pembayaran} juta")



layanan_list= [
    Layanan("Layanan 1  ","Deposito ",2),
    Layanan("Layanan 2  ","Giro     ",4),
    Layanan("Layanan 3  ","Transfer ",1),
    Layanan("Layanan 4  ","Tabungan ",3),
    Layanan("Layanan 5  ","Kredit   ",6),
]
main()