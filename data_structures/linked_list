class Node:
    def __init__(self, data, next = None):
        self._data = data
        self._next = next
        
class SinglyLinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def append(self, data):
        # create a new node with the requested data
        new_node = Node(data)
        # check if the linked list is empty
        if self._head is None:
            # the new node is the head since its the only item in the list now
            self._head = new_node
            self._tail = new_node
        else:
            # add the new node to the end
            self._tail._next = new_node
            # move to the tail to the new node
            self._tail = new_node
        self._size += 1
        
    def prepend(self, data):
        new_node = Node(data)
        
        if self._head is None:
            self._head = new_node
            self._head = new_node
        else:
            new_node._next = self._head
            self._head = new_node
        self._size += 1
        
    def insert(self, data, index):
        # index is at or before the start of the list
        if index <= 0:
            # insert at the beg of the list
            self.prepend(data)
        # index is at or past the end of the list
        elif index >= self._size:
            # insert at the end of the list
            self.append(data)
        # index is in the middle of the list
        else: 
            curr_pos = self._head
            # traverse list until node before index
            for _ in range(index - 1):
                curr_pos = curr_pos._next
                index -= 1
            # insert new node after current pos
            curr_pos._next = Node(data, curr_pos._next)
            self._size += 1
        
    def size(self):
        return self._size
        
    def iter(self):
        curr_pos = self._head
        while curr_pos:
            val = curr_pos._data
            curr_pos = curr_pos._next
            yield val
            
    def __str__(self):
        output = ""
        for item in self.iter():
            output += str(item) + ' '
        return output

num_list = SinglyLinkedList()
num_list.append(10)
num_list.append(20)
num_list.append(30)
num_list.append(40)
num_list.append(50)

curr_pos = num_list._head

print(num_list)
    
print(num_list.size())

num_list.prepend(100)

print(num_list)

num_list.insert(200, 2)

print(num_list)
