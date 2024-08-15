class DoublyLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self._size = 0

    # (a) Add an element at the beginning
    def add_to_beginning(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    # (b) Add an element at the end
    def add_to_end(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self._size += 1

    # (c) Add only unique elements
    def add_unique(self, data):
        if not self.contains(data):
            self.add_to_end(data)
    
    # Helper function to check if the list contains a value
    def contains(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    # (d) Delete the first occurrence of an element
    def delete_first_occurrence(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:  # If head needs to be removed
                    self.head = temp.next
                self._size -= 1
                return
            temp = temp.next

    # (e) Delete all occurrences of an element
    def delete_all_occurrences(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:  # If head needs to be removed
                    self.head = temp.next
                next_temp = temp.next
                temp = next_temp
                self._size -= 1
            else:
                temp = temp.next

    # (f) Add a node after a given node
    def add_after_node(self, target_node, data):
        temp = self.head
        while temp:
            if temp.data == target_node.data:
                new_node = self.Node(data)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                self._size += 1
                return
            temp = temp.next

    # (g) Add a node before a given node
    def add_before_node(self, target_node, data):
        temp = self.head
        while temp:
            if temp.data == target_node.data:
                new_node = self.Node(data)
                new_node.next = temp
                new_node.prev = temp.prev
                if temp.prev:
                    temp.prev.next = new_node
                else:  # If the target node is the head
                    self.head = new_node
                temp.prev = new_node
                self._size += 1
                return
            temp = temp.next

    # (h) Delete a node after a given node
    def delete_after_node(self, target_node):
        temp = self.head
        while temp:
            if temp.data == target_node.data and temp.next:
                node_to_delete = temp.next
                temp.next = node_to_delete.next
                if node_to_delete.next:
                    node_to_delete.next.prev = temp
                self._size -= 1
                return
            temp = temp.next

    # (i) Delete a node before a given node
    def delete_before_node(self, target_node):
        temp = self.head
        while temp:
            if temp.data == target_node.data and temp.prev:
                node_to_delete = temp.prev
                if node_to_delete.prev:
                    node_to_delete.prev.next = temp
                    temp.prev = node_to_delete.prev
                else:  # If the node to delete is the head
                    self.head = temp
                    temp.prev = None
                self._size -= 1
                return
            temp = temp.next

    # Function to print the list (for debugging)
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("---EOL---")
    
    def get_last_node(self):
        if not self.head:
            return None
        curr = self.head
        while curr.next:
            curr= curr.next
        return curr

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node.prev
        successor = node.next
        if predecessor:
            predecessor.next = successor
        else:
            self.head = successor
        if successor:
            successor.prev = predecessor
        self._size -= 1
        element = node.data                             # record deleted element
        # node.prev = node.next = node.data = None      # deprecate node
        return element                                      # return deleted element


import unittest

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_add_to_beginning(self):
        self.dll.add_to_beginning(10)
        self.dll.add_to_beginning(20)
        self.assertEqual(self.dll.head.data, 20)
        self.assertEqual(self.dll.head.next.data, 10)
        self.assertEqual(self.dll.head.next.prev.data, 20)

    def test_add_to_end(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.head.next.prev.data, 10)

    def test_add_unique(self):
        self.dll.add_to_end(10)
        self.dll.add_unique(20)
        self.dll.add_unique(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertIsNone(self.dll.head.next.next)

    def test_delete_first_occurrence(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        self.dll.add_to_end(30)
        self.dll.delete_first_occurrence(20)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 30)
        self.assertIsNone(self.dll.head.next.next)

    def test_delete_all_occurrences(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        self.dll.add_to_end(20)
        self.dll.add_to_end(30)
        self.dll.delete_all_occurrences(20)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 30)
        self.assertIsNone(self.dll.head.next.next)

    def test_add_after_node(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        self.dll.add_after_node(10, 15)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 15)
        self.assertEqual(self.dll.head.next.next.data, 20)

    def test_add_before_node(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        self.dll.add_before_node(20, 15)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 15)
        self.assertEqual(self.dll.head.next.next.data, 20)

    def test_delete_after_node(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        self.dll.add_to_end(30)
        self.dll.delete_after_node(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 30)
        self.assertIsNone(self.dll.head.next.next)

    def test_delete_before_node(self):
        self.dll.add_to_end(10)
        self.dll.add_to_end(20)
        self.dll.add_to_end(30)
        self.dll.delete_before_node(30)
        self.assertEqual(self.dll.head.data, 20)
        self.assertEqual(self.dll.head.next.data, 30)
        self.assertIsNone(self.dll.head.next.next)