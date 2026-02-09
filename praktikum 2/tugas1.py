# ==========================================================
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
# Nama : Ni Kadek Belinda Asty
# NIM  : J0403251055
# Kelas: TPL A / P1
# ==========================================================

nama_file = "stok_barang.txt"


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    stok_dict = {}

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris:
                    kode, nama, stok = baris.split(",")
                    stok_dict[kode.strip()] = {
                        "nama": nama.strip(),
                        "stok": int(stok.strip())
                    }
    except FileNotFoundError:
        # Jika file belum ada, buat file kosong
        with open(nama_file, "w", encoding="utf-8"):
            pass

    return stok_dict


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

    print("Data stok barang berhasil disimpan ke file.")


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    print("\n=== DAFTAR STOK BARANG KANTIN ===")
    print(f"{'Kode':<10} | {'Nama Barang':<20} | {'Stok':>5}")
    print("-" * 40)

    if not stok_dict:
        print("Tidak ada data barang tersedia.")
        return

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<20} | {stok:>5}")


# -------------------------------
# Fungsi: Cari barang
# -------------------------------
def cari_barang(stok_dict):
    # input kode barang
    kode_cari = input("Masukkan kode barang yang ingin dicari: ").strip()

    if kode_cari in stok_dict:
        nama = stok_dict[kode_cari]["nama"]
        stok = stok_dict[kode_cari]["stok"]

        print("\n==== Data barang ditemukan ====")
        print(f"Kode       : {kode_cari}")
        print(f"Nama Barang: {nama}")
        print(f"Stok       : {stok}")
    else:
        print("Barang tidak ditemukan.")


# -------------------------------
# Fungsi: Tambah barang
# -------------------------------
def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()

    # cek apakah kode sudah ada
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    # input nama barang
    nama = input("Masukkan nama barang: ").strip()

    try:
        #cek stok tidak kurang dari 0
        stok_awal = int(input("Masukkan stok awal: "))
        if stok_awal < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return

    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    simpan_stok(nama_file, stok_dict)
    print("Barang berhasil ditambahkan.")


# -------------------------------
# Fungsi: Update stok
# -------------------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate stoknya: ").strip()

    if kode not in stok_dict:
        print("Kode barang tidak ditemukan.")
        return

    try:
        stok_baru = int(input("Masukkan stok baru: "))
        if stok_baru < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return

    stok_lama = stok_dict[kode]["stok"]
    stok_dict[kode]["stok"] = stok_baru

    simpan_stok(nama_file, stok_dict)

    print(f"Stok barang dengan kode {kode} berhasil diubah dari {stok_lama} menjadi {stok_baru}.")


# -------------------------------
# Program Utama
# -------------------------------
def main():
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang")
        print("3. Tambah barang")
        print("4. Update stok")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


# -------------------------------
# Eksekusi Program
# -------------------------------
if __name__ == "__main__":
    main()

