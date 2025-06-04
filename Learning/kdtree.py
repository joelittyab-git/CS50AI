from copy import deepcopy
from vector import Vector2D

class BinaryTree2D:
     def __init__(self, points:list):
          self.points = points
          self.root = None
          
     def construct(self):
          """
          Constructs the 2-D binary tree using the given data points
          """
          cloned = deepcopy(self.points)
          
          parent_value = cloned.pop(0)
          self.root = Node(Vector2D(*parent_value))
          
          for i in cloned:
               self.root.push(Vector2D(*i))
               
          return self.root
     
     def add(self, pos:tuple):
          """Adds a new point to the given points and appends a new Node to the tree"""
          
          
          if len(pos)!=2:
               raise ValueError(f"Invalid arguments. Expected 2 argumens but received {len(pos)}")
          
          self.points.append(pos)
          self.root.push(Vector2D(*pos))
               
               
class Node:
     def __init__(self, value:Vector2D, left = None, right = None):
          self.value:Vector2D = value
          self.right = right
          self.left = left
         
     
     def push(self, value:Vector2D, flag = 1):
          """
          Pushes an element to the current node
          """
          if flag==1:    # x comparisson
               if value.x>self.value.x:
                    if self.right is None:
                         self.right = Node(value)
                         return
                    return self.right.push(value=value,flag=-flag)
               if self.left is None:
                    self.left = Node(value)
                    return
               return self.left.push(value=value, flag=-flag)
          else:
               if value.y>self.value.y: # y comparisson
                    if self.right is None:
                         self.right = Node(value)
                         return
                    return self.right.push(value=value, flag=-flag)
               if self.left is None:
                    self.left = Node(value)
                    return
               return self.left.push(value=value, flag=-flag)