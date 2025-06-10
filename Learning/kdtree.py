from copy import deepcopy
from vector import Vector2D
import math
import heapq

class BinaryTree2D:
     def __init__(self, points:list):
          self.points = points
          self.root = None
          
     def construct(self):
          """
          Constructs the 2-D binary tree using the given data points
          """
          print("Constructing Tree...")
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
          
     def add_vec(self, vector:Vector2D):
          """Adds a new point in the form of a new vector to the tree"""
          
          self.points.append((vector.x,vector.y))
          self.root.push(vector)
               
               
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
          
          
          
def traverse(node:Node,query:Vector2D,k:int = 1, layer = 1, container = None):
     
     if node is None:
          return container
     
     if container is None:
          container = []
     
     '''
     node:(nx,ny)
     query:(qx,qy)
     layer = 1 symbolizing the x dimension since the root node always starts from the x dimension
     '''
     nx = node.value.x
     ny = node.value.y
     qx = query.x
     qy = query.y
     
     # calcualtes the distance from the current node and validates it with existing values
     node_distance = math.sqrt((qx-nx)**2 + (qy-ny)**2)
     
     heapq.heappush(container,(-node_distance, node.value))
     if len(container)>k:
          heapq.heappop(container)
     
          
     if layer==1:   # check against the x coordinates
          goleft = qx<=nx 
          primary = node.left if goleft else node.right
          secondary = node.right if goleft else node.left 
          axis_distance = abs(qx-nx)**2
     else:     
          goleft = qy<=ny
          primary = node.left if goleft else node.right
          secondary = node.right if goleft else node.left
          axis_distance = abs(qy-ny)**2

          
     container = traverse(primary, query, k, -layer, container)
     
     if axis_distance<-container[0][0]:
          container = traverse(secondary, query, k, -layer, container)
     
     return [(-a,b) for a,b in container]

# test
if __name__ == "__main__":
     # Sample points
     import random

     random.seed(42)  # for reproducibility
     data = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(1000)]  # 1000 data points
     
     print(data)

     # Query point
     query = Vector2D(66, 65)
     
     tree = BinaryTree2D(data)
     root = tree.construct()
     k = traverse(root, query, 3)
     print("Query:", query)
     print("Nearest:", k)