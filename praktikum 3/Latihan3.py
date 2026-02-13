# ==========================================
# LATIHAN 3
# Pencarian pada Doubly Linked List
# ==========================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

   
    def search(self, key):
        temp = self.head

        # Jika list kosong
        if temp is None:
            print("Doubly Linked List kosong.")
            return

        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Doubly Linked List")
                return
            temp = temp.next

        # kalo  ga ditemukan
        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List")





dll = DoublyLinkedList()
# node 2,6,9,14
node1 = Node(2)
node2 = Node(6)
node3 = Node(9)
node4 = Node(14)


dll.head = node1

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

print("Masukkan elemen ke dalam Doubly Linked List: 2, 6, 9, 14")
key = int(input("Masukkan elemen yang ingin dicari: "))

dll.search(key)
