"""This module is the implementation of basic datastructures"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        temp = self.head
        self.head = Node(data, temp)
        return

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        return

    def print_list(self):
        temp = self.head
        if temp is None:
            print("list is empty")
            return
        while temp:
            print(f"{temp.data} -->",end=' ')
            temp = temp.next
        return

    def delete_node(self, data):
        temp = self.head
        prev = temp
        while temp:
            if temp.data == data:
                 prev.next = temp.next
                 temp = None
                 return
            prev = temp
            temp = temp.next
        print("Invalid node: node not found")
    def insert_before_node(self, data, new_node):
        prev = temp = self.head
        while temp:
            if temp.data == data:
                prev.next = Node( new_node, temp)
                return
            prev = temp
            temp = temp.next
        print("Invalid node: node not found")
        return

    def insert_after_node(self, data, new_node):
        prev = temp = self.head
        while temp:
            if temp.data == data:
                #prev = temp
                temp.next = Node(new_node, temp.next)
                return
            temp = temp.next
        print("Invalid node: node not found")
        return

"""if __name__ == "__main__":
    #while True:
    #    operation = int(input("Enter number to select the operation given below:"))
    linklist = LinkList()
    linklist.print_list()
    linklist.insert_at_end(25)
    linklist.insert_at_end(50)
    linklist.insert_at_beginning('I am first')
    linklist.insert_at_beginning('No ! I am first')
    linklist.delete_node(50)
    linklist.insert_before_node(25, 15)
    linklist.insert_after_node(15, 18)
    linklist.print_list()
"""





