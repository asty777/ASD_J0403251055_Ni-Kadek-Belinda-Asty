# ==============================
# LATIHAN 1
# Delete Node pada Single Linked List
# ==============================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Elemen tidak ditemukan.")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


sll = SingleLinkedList()
for angka in [1, 2, 3, 4, 5]:
    sll.append(angka)

print("Sebelum dihapus:")
sll.display()

sll.delete_node(3)
print("Setelah hapus 3:")
sll.display()
