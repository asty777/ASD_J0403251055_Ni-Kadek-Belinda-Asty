# ==========================================
# Nama : Ni Kadek Belinda Asty
# NIM : J0403251055
# Kelas : TPL A1
# ==========================================

# ==========================================
# Implementasi dasar : Queue
# ========================================== 

class Node:
    #konstruktor yang dijalanka secara otomatis ketiak class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list 
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

class queue: 
    #buat konstruktor untuk inisialisasi variabel front dan rear 
    def __init__(self):
        self.front = None #Node paling depan 
        self.rear = None #Node paling belakang 
    def is_empty(self):
        return self.front is None

    #Membuat fungsi untuk menambahkan data baru pada bagian paling belakang 
    def enqueue(self, data):
        NodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama 
        if self.is_empty():
            self.front = NodeBaru 
            self.rear = NodeBaru
            return 
        
        #Jika queue tidak kosong maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = NodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = NodeBaru #Jadikan data baru seagai rear 
    def dequeue(self):
        #menghapus data dari depan/front
        data_terhapus = self.front.data #Lihat data paling depan

        #geser front ke node barikutnya 
        self.front = self.front.next

        #Jika setelah geser front menjadi kosong, maka queue kosong
        #rear juga harus jadi none
        if self.front is None: 
            self.rear = None 

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front -> ", end=" ")
        while current is not None: 
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear")


#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()




    