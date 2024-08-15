
from positional_list import PositionalList

class Stack():
    
    def __init__(self):
        self.ls = PositionalList()
    
# • S.push(e): Add element e to the top of stack S.
    def push(self, e):
        self.ls.add_last(e)

# • S.pop(): Remove and return the top element from the stack S; an error
# occurs if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError("empty stack")
        val = self.ls.last().element()
        self.ls.delete(self.ls.last())
        return val
# Additionally, let us define the following accessor methods for convenience:

# • S.top( ): Return a reference to the top element of stack S, without remov-
# ing it; an error occurs if the stack is empty.
    def top(self):
        if self.is_empty():
            raise IndexError("empty stack")
        return self.ls.first().element()
    
# • S.is empty( ): Return True if stack S does not contain any elements.
    def is_empty(self):
        return len(self.ls) == 0
    
# • len(S): Return the number of elements in stack S; in Python, we implement
# this with the special method len .
    def __len__(self):
        return len(self.ls)

import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(10)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.top(), 10)

    def test_pop(self):
        self.stack.push(20)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 20)
        self.assertTrue(self.stack.is_empty())

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_top(self):
        self.stack.push(30)
        self.assertEqual(self.stack.top(), 30)
        self.assertEqual(len(self.stack), 1)

    def test_top_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.top()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(40)
        self.assertFalse(self.stack.is_empty())

    def test_len(self):
        self.assertEqual(len(self.stack), 0)
        self.stack.push(50)
        self.assertEqual(len(self.stack), 1)
        self.stack.push(60)
        self.assertEqual(len(self.stack), 2)
        self.stack.pop()
        self.assertEqual(len(self.stack), 1)


unittest.main()