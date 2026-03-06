# Nama  : Ni Kadek Belinda Asty
# NIM   : J04032501055
# Kelas : TPL A1
# Soal Pengurutan - Menggunakan Buble Sort
# ==========================================================

def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i] < data[i+1]:   # descending
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
bubbleSort(data)

print("Data setelah diurutkan:", data)
print("5 nilai tertinggi:", data[:5])
print("Kandidat yang lolos : 7, 4, 2, 9, 8")

