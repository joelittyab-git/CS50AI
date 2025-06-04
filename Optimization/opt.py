import random
import math

class Space:
     def __init__(self, length, width, n_hospitals):
          self.length = length
          self.width = width
          self.n_hospitals = n_hospitals
          self.houses = set()
          self.hospitals = set()
          
     def add_house(self, x, y):
          """
          Adds a house to the board which has a coordinate (x,y)
          """
          
          # coordinate validation
          assert ((x>=0 and y>=0) and 
               (x<self.length and y<self.width))
          
          self.houses.add((x,y))
          
     def _place_entity(self, x,y):
          self.hospitals.add((x,y))
          
          
     def available_spaces(self):
          """
          Returns a set of coordinates that are empty
          """
          
          spaces = list()
          
          for i in range(self.length):
               for j in range(self.width):
                    if (i, j) not in self.houses and (i,j) not in self.hospitals:
                         spaces.append((i,j))
                         
          return spaces
          
     def neighbours(self, x, y):
          """
          Returns the list neighbouring coordinates (diagonals included)
          """
          
          neighbour = list()
          for i in range(x - 1, x + 2):      # x
               if i < 0 or i >= self.length:
                    continue
               for j in range(y - 1, y + 2): # y
                    if j < 0 or j >= self.width:
                         continue
                    if ((i, j) != (x, y) and
                        (i,j) not in self.houses and
                        (i,j) not in self.hospitals
                    ): 
                         neighbour.append((i, j))
          return neighbour
     
     def cost(self):
          """
          Returns the cost the current 
          """
          tert = list()
          c = 0
          for house in self.houses:
               closest = math.inf
               for entity in self.hospitals:
                    e_x,e_y = entity
                    h_x,h_y = house
                    
                    distance = abs(h_x-e_x) + abs(h_y-e_y)
                    if distance<closest:closest = distance
               tert.append(closest)

          return sum(tert)
                         
                    

          
     def start(self, iterations:int = 100):
          pass
                              
               
               
     