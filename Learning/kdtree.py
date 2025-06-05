from copy import deepcopy
from vector import Vector2D
import math


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
          
          
          
def traverse(node:Node,query:Vector2D, best_point:Vector2D = None, best_cost = math.inf, layer = 1):
     
     if node is None:
          return best_point,best_cost
     
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
     if node_distance<best_cost:
          best_cost = node_distance
          best_point = deepcopy(node.value)
          
     if layer==1:   # check against the x coordinates
          goleft = qx<=nx 
          primary = node.left if goleft else node.right
          secondary = node.right if goleft else node.left 
          axis_distance = abs(qx-nx)
     else:     
          goleft = qy<=ny
          primary = node.left if goleft else node.right
          secondary = node.right if goleft else node.left
          axis_distance = abs(qy-ny)

          
     best_point,best_cost = traverse(primary, query,best_point,best_cost,-layer)
     
     if  axis_distance<best_cost:
          best_point, best_cost = traverse(secondary, query, best_point, best_cost, -layer)
     
     return best_point,best_cost

# test
if __name__ == "__main__":
     # Sample points
     data = [
          (12, 30), (5, 25), (17, 45), (9, 40), (50, 30), (60, 20), (80, 55), (25, 10), (30, 35), (70, 70),
          (85, 15), (10, 50), (40, 80), (55, 25), (65, 65), (45, 20), (15, 5), (20, 60), (90, 40), (95, 90),
          (35, 5), (48, 48), (33, 77), (11, 23), (22, 11), (75, 75), (32, 32), (18, 36), (8, 8), (27, 45),
          (67, 22), (29, 31), (19, 19), (31, 50), (23, 33), (13, 13), (38, 65), (59, 59), (39, 39), (73, 28),
          (2, 2), (44, 44), (6, 60), (3, 12), (26, 26), (91, 91), (14, 66), (63, 63), (76, 76), (99, 10),
          (12, 18), (24, 24), (28, 28), (36, 36), (42, 42), (52, 52), (64, 64), (66, 66), (68, 68), (71, 71),
          (74, 74), (77, 77), (78, 78), (79, 79), (81, 81), (82, 82), (83, 83), (84, 84), (86, 86), (87, 87),
          (88, 88), (89, 89), (92, 92), (93, 93), (94, 94), (96, 96), (97, 97), (98, 98), (100, 100), (1, 1),
          (4, 4), (7, 7), (16, 16), (21, 21), (34, 34), (37, 37), (41, 41), (43, 43), (46, 46), (47, 47),
          (49, 49), (51, 51), (53, 53), (54, 54), (56, 56), (57, 57), (58, 58), (61, 61), (62, 62), (69, 69)
     ]

     # Query point
     query = Vector2D(66, 65)
     
     tree = BinaryTree2D(data)
     root = tree.construct()
     best, cost = traverse(root, query)

     print("Query:", query)
     print("Nearest:", best)
     print("Distance:", round(cost, 4))