class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class SingleLinkedList:

  def __init__(self):
    self.head = None

#   def length(self):
#     if not self.head:
#       return 0
#     else:
#       count = 1
#       curr = self.head
#       while curr.next:
#         count = count+1
#         curr = curr.next
#       return count

  def length(self):
    count = 0
    if self.head:
      count = 1
      curr = self.head
      while curr.next:
        count = count+1
        curr = curr.next
    return count


  def print_list(self):
    ls =[]
    if self.head:
      curr = self.head
      while curr.next:
        ls.append(curr.value)
        curr = curr.next
      ls.append(curr.value)
    print(ls)

  # to add an element in the beginning
  def append_first(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

  #  to add an element in the end
  def append_last(self, value):
    new_node = Node(value)
    last = self.get_last_node()
    if last:
        last.next = new_node
    else:
        self.head = new_node

  def get_last_node(self):
    if not self.head:
      return None
    curr = self.head
    while curr.next:
      curr= curr.next
    return curr

  def get_last_node_value(self):
    return self.get_last_node().value
  # to check if an element exists
  def contains(self, value):
    curr = self.head
    while(curr):
      if curr.value == value:
        return True
      curr = curr.next
    return False

  # to add only unique elements
  def add_if_unique(self, value):
    if not self.contains(value):
      self.append_last(value)

  # to delete the first occurre-nce of an element
  def delete_one(self,value):
    if not self.head:
      return
    if self.head.value == value:
      self.head = self.head.next
      return
    curr = self.head
    while curr.next and curr.next.value!=value:
      curr = curr.next
    if curr.next:
        curr.next = curr.next.next

  # to delete all the occurrences of an element
  def delete_all(self, value):
    if not self.head:
        return
    while self.head.value==value:
        self.head = self.head.next 
    curr = self.head
    while curr.next:
        if curr.next.value==value:
            curr.next = curr.next.next
        else:
            curr = curr.next

  def add_after(self, target, insert_value):
    curr = self.head
    while  curr:
        if curr.value == target:
            new_node = Node(insert_value)
            new_node.next = curr.next
            curr.next = new_node
            return
        curr = curr.next
  
  def add_before(self, target, insert_value):
    curr = self.head
    prev = None
    if not curr:
        return
    if curr.value == target:
            new_node = Node(insert_value)
            new_node.next = curr
            self.head = new_node
            return
    prev = curr
    curr = curr.next
    while curr:
        if curr.value == target:
            new_node = Node(insert_value)
            new_node.next = curr
            prev.next = new_node
            return
        prev = curr
        curr = curr.next
            
  def delete_after(self, target):
    curr = self.head
    while  curr:
        if curr.value == target and curr.next:
            curr.next = curr.next.next
            return
        curr = curr.next
  
  def delete_before(self, target):
    curr = self.head
    prev = None
    if not curr:
        return
    if curr.value == target:
        return
    if curr.next and curr.next.value == target:
        self.head = curr.next
        return

    prev = curr
    curr = curr.next
    succ = curr.next
    while succ:
      if succ.value == target:
        prev.next = succ
        return
      prev = curr
      curr = curr.next
      succ = succ.next



import unittest
case = unittest.TestCase()

list = SingleLinkedList()
case.assertEqual(list.length(),0)
list.print_list()
case.assertEqual(list.contains(5), False)
list.append_first(5)
list.print_list()
case.assertEqual(list.contains(5), True)
case.assertEqual(list.length(),1)
list.append_last(10)
case.assertEqual(list.get_last_node_value(), 10)
list.print_list()
case.assertEqual(list.length(),2)
list.append_first(2)
list.print_list()
case.assertEqual(list.length(),3)
list.add_if_unique(2)
list.print_list()
list.append_first(7)
list.print_list()
case.assertEqual(list.length(),4)
case.assertEqual(list.contains(5),True)
case.assertEqual(list.contains(90),False)
list.append_first(5)
list.append_last(8)
list.append_last(5)
list.append_last(5)
list.print_list()
list.delete_all(5)
list.print_list()
case.assertEqual(list.length(),4)
list.add_after(3,2)
list.print_list()
list.add_after(10,9)
list.print_list()
list.add_before(3,2)
list.print_list()
list.add_before(10,9)
list.print_list()
list.add_before(8,0)
list.print_list()
list.add_before(7,0)
list.print_list()
print("===delete operation===")
list.delete_after(3)
list.print_list()
list.delete_after(10)
list.print_list()
list.delete_before(3)
list.print_list()
list.delete_before(10)
list.print_list()
list.delete_before(8)
list.print_list()
list.delete_before(7)
list.print_list()
