
# class Node:
#         def __init__(self, val, prev=None, next=None):
#             self.element = val
#             self.prev = prev
#             self.next = next

from doubly_linked_list import DoublyLinkedList

# Positional List
class PositionalList(DoublyLinkedList):

    class Position:
        def __init__(self, node, list):
            self.node  = node
            self.list = list
              
        # • p.element(): Return the element stored at position p.
        def element(self):
            return self.node.data

        def get_node(self):
            return self.node
        
    def _create_position(self, node):
        if node:
            return self.Position(node, self)
        else:
            return None
    
    # • L.first(): Return the position of the first element of L,or None if L isempty.
    def first(self):
        return self._create_position(self.head)

    # • L.last(): Return the position of the last element of L,or None if L is empty.
    def last(self):
        return self._create_position(self.get_last_node())
    
    # • L.before(p): Return the position of L immediately before position p, or
    # None if p is the first position.
    def before(self, p):
        return self._create_position(p.node.prev)

    # • L.after(p): Return the position of L immediately after position p, or None
    # if p is the last position.
    def after(self, p):
        return self._create_position(p.node.next)

    # • L.is empty( ): Return True if list L does not contain any elements.
    def is_empty(self):
        return self._size==0

    # • len(L): Return the number of elements in the list.
    def __len__(self):
        return self._size

    # • iter(L): Return a forward iterator for the elements of the list. See Section
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
        cursor = self.after(cursor)
    
    # 1.8 for discussion of iterators in Python.

    # The positional list ADT also includes the following update methods:

    # • L.add first(e): Insert a new element e at the front of L, returning the
    # position of the new element.
    def add_first(self, e):
        self.add_to_beginning(e)
        return self._create_position(self.head) 
    
    # • L.add last(e): Insert a new element e at the back of L, returning the
    # position of the new element.
    def add_last(self, e):
        self.add_to_end(e)
        return self._create_position(self.get_last_node()) 

    # • L.add before(p, e): Insert a new element e just before position p in L,
    # returning the position of the new element.
    def add_before(self, p, e):
        self.add_before_node(p.get_node(),e)
        return self._create_position(p.get_node().prev) 

    # • L.add after(p, e): Insert a new element e just after position p in L, re-
    # turning the position of the new element.
    def add_after(self, p, e):
        self.add_after_node(p.get_node(),e)
        return self._create_position(p.get_node().next) 

    # • L.replace(p, e): Replace the element at position p with element e, return-
    # ing the element formerly at position p.
    def replace(self, p, e):
        val = p.element()
        p.get_node().data = e
        return val
    
    # • L.delete(p): Remove and return the element at position p in L, invalidating
    # the position.
    def delete(self, p):
        val = p.element()
        self._delete_node(p.get_node())
        return val
    

import unittest

class TestPositionalList(unittest.TestCase):

    def setUp(self):
        self.plist = PositionalList()

    def test_is_empty(self):
        self.assertTrue(self.plist.is_empty())
        self.plist.add_first(10)
        self.assertFalse(self.plist.is_empty())

    def test_len(self):
        self.assertEqual(len(self.plist), 0)
        self.plist.add_first(10)
        self.plist.add_last(20)
        self.assertEqual(len(self.plist), 2)

    def test_add_first(self):
        pos = self.plist.add_first(10)
        self.assertEqual(pos.element(), 10)
        self.assertEqual(self.plist.first().element(), 10)

    def test_add_last(self):
        pos = self.plist.add_last(20)
        self.assertEqual(pos.element(), 20)
        self.assertEqual(self.plist.last().element(), 20)

    def test_before_and_after(self):
        pos1 = self.plist.add_first(10)
        pos2 = self.plist.add_last(20)
        pos3 = self.plist.add_after(pos1, 15)

        self.assertEqual(self.plist.before(pos2).element(), 15)
        self.assertEqual(self.plist.after(pos1).element(), 15)
        self.assertEqual(self.plist.before(pos1), None)
        self.assertEqual(self.plist.after(pos2), None)

    def test_add_before_and_after(self):
        pos1 = self.plist.add_first(10)
        pos2 = self.plist.add_last(20)
        pos3 = self.plist.add_before(pos2, 15)

        self.assertEqual(pos3.element(), 15)
        self.assertEqual(self.plist.before(pos2).element(), 15)
        self.assertEqual(self.plist.after(pos1).element(), 15)

    def test_replace(self):
        pos1 = self.plist.add_first(10)
        old_value = self.plist.replace(pos1, 20)
        self.assertEqual(old_value, 10)
        self.assertEqual(pos1.element(), 20)

    def test_delete(self):
        pos1 = self.plist.add_first(10)
        pos2 = self.plist.add_last(20)
        print(self.plist.print_list())
        deleted_value = self.plist.delete(pos1)
        print(self.plist.print_list())

        self.assertEqual(deleted_value, 10)
        self.assertEqual(len(self.plist), 1)
        self.assertEqual(self.plist.first().element(), 20)

    # def test_iter(self):
    #     self.plist.add_first(10)
    #     self.plist.add_last(20)
    #     self.plist.add_last(30)

    #     elements = list(iter(self.plist))
    #     self.assertEqual(elements, [10, 20, 30])

if __name__ == '__main__':
    unittest.main()

