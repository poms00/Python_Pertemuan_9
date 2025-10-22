# Latihan B — Validasi ringan

class Dosen:
    def __init__(self, nidn, nama):
        # Validasi panjang dan digit
        if len(nidn) == 10 and nidn.isdigit():
            self.nidn = nidn
        else:
            print("⚠️ Error: NIDN harus 10 digit angka.")
            self.nidn = "INVALID"

        self.nama = nama

    def info(self):
        print(f"Dosen {self.nama} - {self.nidn}")


# --- Contoh penggunaan ---
d1 = Dosen("1234567890", "Pak Triyono")   # valid
d2 = Dosen("1234ABC", "Bu Agustina")       # tidak valid

d1.info()
d2.info()
