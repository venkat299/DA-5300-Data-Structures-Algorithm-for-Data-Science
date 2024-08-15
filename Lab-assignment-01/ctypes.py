
import ctypes
import sys
from abc import abstractmethod

class DynamicArray:
    def __init__ (self):
        self.n = 0 # count actual elements
        self.capacity = 1 # default array capacity
        self.A = self._makearray(self.capacity) 

    def len(self):
        return self.n

    def size(self):
        return sizeof(self.A)
    
    def __getitem__ (self, k):
        if not 0 <= k < self.n:
            raise IndexError('invalid index')
        return self.A[k] 
    
    def append(self, obj):
        if self.n == self.capacity: 
            self._resize(2* self.capacity)
        self.A[self.n] = obj
        self.n += 1

    def _resize(self, c): 
        B = self._makearray(c) # new (bigger) array
        for k in range(self.n): # for each existing value
            B[k] = self.A[k]
        self.A = B # use the bigger array
        self.capacity = c

    @abstractmethod
    def _makearray(self, c): # nonpublic utitity
        #”””Return new array with capacity c.”””
        return (c*ctypes.py_object)() 
    
class DynamicArrayInt(DynamicArray):
    def __init__(self):
        super().__init__()

    def _makearray(self, c):  
        return (c*ctypes.c_int)()  # int

import sys 
data= DynamicArrayInt()
n=10000
for k in range(n):
# provides getsizeof function
# NOTE: must fix choice of n # number of elements
# actual size in bytes
#   print(k)
  a = data.len()
  b = data.size()
#   print(a,b)
  print("Length: {}; Size in bytes: {}".format(a, b)) 
  data.append(1) # increase length by one