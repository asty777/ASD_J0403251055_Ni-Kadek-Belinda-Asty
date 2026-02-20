# ==========================================
# Nama : Ni Kadek Belinda Asty
# NIM : J0403251055
# Kelas : TPL A1
# ==========================================

# ==========================================
# Implementasi dasar : Stack
# ========================================== 

class Node:
    #konstruktor yang dijalanka secara otomatis ketiak class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list 
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#Stack ada operasi push(Memasukan head baru) dan pop(menghapus head)
# A -> B -> C -> None 

class stack: 
    def __init__(self):
        self.top = None #Top menunjuk ke node paling atas (Awalnya kosong)
    
    def is_empty(self): 
        return self.top is None

    def push(self,data): #memasukan data baru pada stack
        #1 Membuat node baru 
        NodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class node 

        #2 Node baru menunjuk ke top yang lama (head lama)
        NodeBaru.next = self.top 
        
        #3 geser top/head pindah ke node baru 
        self.top = NodeBaru

    def pop(self): #mengambil atau menghapus node paling atas(top/head)
        if self.is_empty():
            print("stack kosong, tidak bisa pop")
            return None
        DataTerhapus = self.top.data #soroti bagian top dan simpan di variabel 
        self.top = self.top.next
        return DataTerhapus
    
    def peek(self): 
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty(): 
         return None 
        return self.top.data
    


    def tampilkan(self):
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next  
        print("None")

#Instantiasi class Stack 

s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())



