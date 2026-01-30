#============================================================
# Praktikum 1 Konsep ADT dan File Handling 
# Latihan dasar 1 Membaca seluruh isi file data
#============================================================

print("===Membuka file dalam satu string===")
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    isi_file = file.read()
print(isi_file)

print("tipe data", type(isi_file))  #menampilkan tipe data isi_file

print("===Membuka file per baris===")
jumlah_baris = 0
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() 
        print("baris ke ", jumlah_baris)
        print("isinya :", baris)


#============================================================
# Praktikum 1 Konsep ADT dan File Handling 
# Latihan dasar 2 Parsing baris menjadi data satuan dan menampilkan dalam bentuk kolom data 
#============================================================


with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah data variabel satuan dan simpan ke 
        print("NIM  :", nim, "| Nama : ", nama, "| Nilai :", nilai) #menampilkan satuan data dalam bentuk kolom 
       

#============================================================
# Praktikum 1 Konsep ADT dan File Handling 
# Latihan 3 membaca data dan menyimpannya ke dalam struktur data list 
#============================================================


data_list = []
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah data variabel satuan dan simpan ke 
        print("NIM  :", nim, "| Nama : ", nama, "| Nilai :", nilai) #menampilkan satuan data dalam bentuk kolom 
        data_list.append([nim, nama, int(nilai)]) #menyimpan data satuan ke dalam list
print("====Menampilkan list====")
print(data_list)
print("Contoh record ke 1,", data_list[0])
print("Contoh record ke 2,", data_list[1])


#============================================================
# Praktikum 1 Konsep ADT dan File Handling 
# Latihan 4 membaca data dan menyimpannya ke dalam struktur data dictionary 
#============================================================


data_dict = {} #inisialisasi dictionary 
with open('data_mahasiswa.txt', 'r', encoding='utf-8') as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah data variabel satuan dan simpan ke 
        data_dict[nim] = {
            'nama': nama,
            'nilai': int(nilai)
        } 
print("====Menampilkan Data Dictionary====")
print(data_dict)


