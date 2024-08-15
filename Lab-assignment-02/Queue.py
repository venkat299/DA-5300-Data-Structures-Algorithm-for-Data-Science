
from positional_list import PositionalList

class Queue():
    
    def __init__(self):
        self.ls = PositionalList()
# • Q.enqueue(e): Add element e to the back of queue Q.

    def enqueue(self, e):
        self.ls.add_first(e)
    
# • Q.dequeue(): Remove and return the first element from queue Q; an error
# occurs if the queue is empty.

    def dequeue(self):
        if len(self.ls)==0:
            raise ValueError('queue is empty')
        return self.ls.delete(0)

# The queue ADT also includes the following supporting methods (with first
# being analogous to the stack’s top method):

# • Q.first(): Return a reference to the element at the front of queue Q, without
# removing it; an error occurs if the queue is empty.

    def first(self):
        return self.ls.first().element()
    
# • Q.is empty( ):Return True if queue Q does not contain any elements.
    def empty(self):
        return len(self.ls) == 0

# • len(Q): Return the number of elements in queue Q; in Python, we imple-
# ment this with the special method len .
    def __len__(self):
        return len(self.ls)

import unittest

class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(len(self.queue), 3)

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.dequeue(), 30)
        self.assertTrue(self.queue.is_empty())

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_first(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.first(), 10)
        self.queue.dequeue()
        self.assertEqual(self.queue.first(), 20)

    def test_first_empty(self):
        with self.assertRaises(IndexError):
            self.queue.first()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_len(self):
        self.assertEqual(len(self.queue), 0)
        self.queue.enqueue(10)
        self.assertEqual(len(self.queue), 1)
        self.queue.enqueue(20)
        self.assertEqual(len(self.queue), 2)
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 1)
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 0)

unittest.main()