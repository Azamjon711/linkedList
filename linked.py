class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def insert(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current.next and count < position:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node

    def append(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode

        last = self.head
        while last.next:
            last = last.next
        last.next = newNode


data = list(range(10))
linked = LinkedList()
a = Node(data[0])
linked.head = a
for i in range(1, len(data)):
    b = Node(data[i])
    a.next = b
    a = b

# linked.printList()

# linked.push(6)
# linked.printList()

# linked.insert(7, 5)
# linked.printList()

# linked.append(15)
# linked.printList()

# linked.push(78)
# linked.printList()

# linked.insert(36, 9)
# linked.printList()

# linked.append(32)
# linked.printList()
