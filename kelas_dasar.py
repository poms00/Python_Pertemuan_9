# Latihan A — Kelas Dasar

class Dosen:
    # __init__ adalah konstruktor (otomatis dipanggil saat objek dibuat)
    def __init__(self, nidn, nama):
        self.nidn = nidn   # atribut NIDN
        self.nama = nama   # atribut nama

    # method untuk menampilkan info dosen
    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")


# --- Membuat 2 objek dosen ---
d1 = Dosen("1234567890", "Pak Triyono")
d2 = Dosen("0987654321", "Bu Agustina")

# --- Panggil method info() ---
d1.info()
d2.info()
