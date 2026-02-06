#============================================================
# Praktikum 2 : Konsep ADT dan File Handling
# Latihan 1 : Membuat fungsi Load data
#============================================================

# Variabel menyimpan data 
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file): 
    data_dict = {}  # inisialisasi data dictionary 
    with open(nama_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            if baris:  # memastikan tidak membaca baris kosong
                nim, nama, nilai = baris.split(",")
                data_dict[nim.strip()] = {
                    "nama": nama.strip(),
                    "nilai": int(nilai.strip())
                }
    return data_dict


#============================================================
# Praktikum 2 : Konsep ADT dan File Handling
# Latihan 2 : membuat header tabel
#============================================================

def tampilkan_data(data_dict):
    print("\n==DAFTAR MAHASISWA ===")
    print(f"{'nim':<12} | {'nama':<12} | {'nilai':>5}")
    print("-" * 35)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<12} | {nama:<12} | {nilai:>5}")


#============================================================
# Praktikum 2 : Konsep ADT dan File Handling
# Latihan 3 : membuat fungsi mencari data
#============================================================

# Membuat fungsi pencarian data 

def cari_data(data_dict):
    # pencarian data berdasarkan nim sebagai keys dictionary 
    # input nim mahasiswa yang akan dicari
    nim_cari = input("Masukan nim mahasiswa yang ingin dicari : ").strip()

    if nim_cari in data_dict: 
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("==== Data mahasiswa ditemukan ====")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukan benar!")  


#============================================================
# Praktikum 2 : Konsep ADT dan File Handling
# Latihan 4 : membuat fungsi Update Data 
#============================================================

# Membuat fungsi update data 

def ubah_data(data_dict): 
    # awali dengan mencari nim / data mahasiswa yang ingin diubah datanya 

    nim = input("Masukan nim mahasiwa yang ingin diubah datanya: ").strip()

    if nim not in data_dict: 
        print("NIM tidak ditemukan. Update dibatalkan")
        return  # Keluar dari fungsi jika NIM tidak ditemukan

    try:
        nilai_baru = int(input("Masukan nilai baru 0-100 : ").strip())
    except ValueError:
        print("Input nilai tidak valid. Update dibatalkan.")
        return

    if nilai_baru < 0 or nilai_baru > 100: 
        print("Nilai harus 0-100. Update dibatalkan")
        return

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Data mahasiswa dengan NIM {nim} berhasil diubah dari nilai {nilai_lama} menjadi {nilai_baru}")


#============================================================
# Praktikum 2 : Konsep ADT dan File Handling
# Latihan 5 : Fungsi menyimpan data ke file
#============================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
    print("\nData Berhasil disimpan ke file", nama_file)


#============================================================
# Praktikum 2 : Konsep ADT dan File Handling
#  Latihan 6 : Menu
#============================================================

def main():
    data = baca_data(nama_file)

    while True:
       print("\nMenu:")
       print("1. Tampilkan Data")
       print("2. Cari Data")
       print("3. Ubah Data")
       print("4. Keluar")

       pilihan = input("Pilih menu (1-4): ").strip()

       if pilihan == "1":
           tampilkan_data(data)

       elif pilihan == "2":
           cari_data(data)

       elif pilihan == "3":
           ubah_data(data)
           simpan_data(nama_file, data)

       elif pilihan == "4":
           print("Terima kasih!")
           break

       else:
           print("Pilihan tidak valid. Silakan coba lagi.")



if __name__ == "__main__":
    main()

