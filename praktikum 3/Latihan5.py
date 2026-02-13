# ==========================================
# LATIHAN 5
# Reverse Single Linked List
# ==========================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class SingleLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head

     
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  

    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")





data_input = input("Masukkan elemen untuk Linked List: ")

sll = SingleLinkedList()


elements = data_input.split(",")

prev_node = None
for item in elements:
    value = int(item.strip())
    new_node = Node(value)

    if sll.head is None:
        sll.head = new_node
    else:
        prev_node.next = new_node

    prev_node = new_node


print("Linked List sebelum dibalik: ", end="")
sll.display()

sll.reverse()

print("Linked List setelah dibalik: ", end="")
sll.display()
