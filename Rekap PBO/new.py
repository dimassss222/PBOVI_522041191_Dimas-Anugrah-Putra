class Penduduk:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def info_penduduk(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Alamat: {self.alamat}"


class Pelajar(Penduduk):
    def __init__(self, nama, umur, alamat, nis):
        super().__init__(nama, umur, alamat)
        self.nis = nis

    def info_pelajar(self):
        return f"{super().info_penduduk()}, NIS: {self.nis}"


class Guru(Penduduk):
    def __init__(self, nama, umur, alamat, nip):
        super().__init__(nama, umur, alamat)
        self.nip = nip

    def info_guru(self):
        return f"{super().info_penduduk()}, NIP: {self.nip}"


class MataPelajaran:
    def __init__(self, nama_pelajaran, kode_pelajaran):
        self.nama_pelajaran = nama_pelajaran
        self.kode_pelajaran = kode_pelajaran
        self.pelajar = []

    def tambah_pelajar(self, pelajar):
        self.pelajar.append(pelajar)

    def info_pelajaran(self):
        nama_pelajar = ', '.join([p.nama for p in self.pelajar])
        return f"Pelajaran: {self.nama_pelajaran}, Kode: {self.kode_pelajaran}, Pelajar: {nama_pelajar}"


class Sekolah:
    def __init__(self, nama_sekolah, alamat_sekolah):
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah
        self.guru = []

    def tambah_guru(self, guru):
        self.guru.append(guru)

    def info_sekolah(self):
        nama_guru = ', '.join([g.nama for g in self.guru])
        return f"Sekolah: {self.nama_sekolah}, Alamat: {self.alamat_sekolah}, Guru: {nama_guru}"


# penggunaan
pelajar1 = Pelajar("Ani", 15, "Jl. Merdeka 10", "S123")
guru1 = Guru("Budi", 30, "Jl. Guru 5", "G001")

pelajaran1 = MataPelajaran("Matematika", "MTK101")
pelajaran1.tambah_pelajar(pelajar1)

sekolah1 = Sekolah("SMA Negeri 1", "Jl. Pendidikan 2")
sekolah1.tambah_guru(guru1)

print(pelajar1.info_pelajar())
print(guru1.info_guru())
print(pelajaran1.info_pelajaran())
print(sekolah1.info_sekolah())