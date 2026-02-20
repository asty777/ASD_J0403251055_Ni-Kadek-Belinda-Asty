# ==========================================
# Nama : Ni Kadek Belinda Asty
# NIM : J0403251055
# Kelas : TPL A1
# ==========================================

# ==========================================
# Implementasi dasar : Node pada Linked List
# ==========================================

class Node:
    #konstruktor yang dijalanka secara otomatis ketiak class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list 
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#1) cara membuat node dengan instantiasi class node 
#Contoh node terpisah
NodeA = Node("A")
NodeB = Node("B")
NodeC = Node("C")

#Contoh membuat Linked List 

#2) Mendefinisikan head dan Menghubungkan Node : A->B->C->None
head = NodeA
NodeA.next = NodeB
NodeB.next = NodeC

#3) Traversal : Menelusuri node dari head sampai ke none 
current = head 
while current is not None: 
    print(current) #Menampilkan data pada node
    current = current.next #Pindah ke node berikutnuya 

 













