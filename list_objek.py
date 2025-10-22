# Latihan D — List objek

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def info(self):
        print(f"{self.nama} - {self.nim}")


# Membuat list mahasiswa
daftar_mhs = [
    Mahasiswa("Desta", "2310001"),
    Mahasiswa("Vicky", "2310002"),
    Mahasiswa("Kahfi", "2310003"),
    Mahasiswa("Arsa", "2310004")
]

# Cetak hanya yang namanya huruf awal D atau E
print("Mahasiswa dengan nama awal D atau E:")
for mhs in daftar_mhs:
    if mhs.nama[0].upper() in ["D", "E"]:
        mhs.info()
