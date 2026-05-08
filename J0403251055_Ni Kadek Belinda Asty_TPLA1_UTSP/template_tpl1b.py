# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Ni Kadek Belinda Asty
# NIM     : J0403251055
# Kelas   : TPL A1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}
    # TODO: Implementasikan kode pembacaan file di sini

    try:
        with open(nama_file, "r") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    kode, judul, harga = baris.split(",")
                    database_buku[kode] = {
                        "judul": judul,
                        "harga": int(harga)
                    }
    except FileNotFoundError:
        print("File tidak ditemukan!")

    return database_buku


# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
         self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        # TODO: Implementasikan penambahan node

        node_baru = Node(judul)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        # TODO: Implementasikan traversal linked list

        if self.head is None:
            print("Belum ada buku promosi.")
            return

        current = self.head
        nomor = 1

        while current:
            print(f"{nomor}. {current.judul}")
            current = current.next
            nomor += 1


# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        # TODO: Implementasikan prinsip FIFO

        self.antrean.append(nama_pelanggan)
        print(nama_pelanggan, "masuk ke dalam antrean")

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        # TODO: Implementasikan prinsip FIFO

        if len(self.antrean) == 0:
            print("Antrean kosong")
        else:
            pelanggan = self.antrean.pop(0)
            print(pelanggan, "sedang dilayani")


# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    # TODO: Implementasikan algoritma sorting secara manual

    data = list_harga.copy()

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\n--- Daftar Katalog Buku ---")
            print("\nKatalog Buku:", data_buku)

        elif pilihan == '2':
            print("\n--- Kelola Daftar Buku Promosi ---")
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            print("\n--- KELOLA ANTREAN KASIR ---")
            print("1. Tambah Antrean")
            print("2. Layani Pelanggan")

            pilih_antrean = input("Pilih (1-2): ")

            if pilih_antrean == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)

            elif pilih_antrean == '2':
                antrean_toko.layani_pelanggan()

            else:
                print("Pilihan tidak valid!")

        elif pilihan == '4':
            print("\n--- Laporan Penjualan ---")
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()