# Latihan C — Komposisi mini

class Ruang:
    def __init__(self, kode, kapasitas):
        self.kode = kode
        self.kapasitas = kapasitas


class KelasKuliah:
    def __init__(self, kode_kelas, ruang):
        self.kode_kelas = kode_kelas
        self.ruang = ruang
        self.peserta = []  # list kosong untuk menyimpan nama peserta

    def tambah_peserta(self, nama):
        # Cek apakah kapasitas sudah penuh
        if len(self.peserta) < self.ruang.kapasitas:
            self.peserta.append(nama)
            print(f"{nama} berhasil ditambahkan ke {self.kode_kelas}.")
        else:
            print(f"❌ Tidak bisa menambah {nama}, kapasitas penuh ({self.ruang.kapasitas}).")

    def info(self):
        print(f"Kelas {self.kode_kelas} di ruang {self.ruang.kode}")
        print(f"Peserta ({len(self.peserta)}/{self.ruang.kapasitas}): {', '.join(self.peserta)}")


# --- Contoh penggunaan ---
r1 = Ruang("LabA", 2)
kelas1 = KelasKuliah("PBO1", r1)

kelas1.tambah_peserta("Desta")
kelas1.tambah_peserta("Vicky")
kelas1.tambah_peserta("Arsa")  # melebihi kapasitas

kelas1.info()
