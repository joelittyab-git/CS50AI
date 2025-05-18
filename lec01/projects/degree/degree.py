import csv
from dotenv import load_dotenv
import os
from copy import deepcopy

load_dotenv()

movies = {}
people = {}
stars = {}

def load_file_data():
     M_PATH = os.getenv('MOVIES_PATH')
     
     with open(M_PATH, "r") as file:
          reader = csv.reader(file)
          for read in reader:
               movies[read[0]] = [
               read[1],
               read[2]
          ]

     P_PATH = os.getenv('PEOPLE_PATH')
     with open(P_PATH, 'r') as file:
          reader = csv.reader(file)
          for read in reader:
               people[read[0]] = [
                    read[1],
                    read[2]
               ]
               
     S_PATH = os.getenv('STARS_PATH')
     with open(S_PATH, 'r') as file:
          reader = csv.reader(file)
          for read in reader:
               stars[read[0]] = read[1]
          
load_file_data()

def get_name_for(id:int):
     return people[str(id)][0]

# AI impl. ----------------
class State:
     def __init__(self,parent, name:str, cost:int, action, id):
          self.parent = parent     # Parent state
          
          self.name = name 
          self.cost = cost
          self.action = action
          self.id = id
          
     def get_name(self):
          return deepcopy(self.name)
     
     def get_cost(self):
          return deepcopy(self.cost)
     
     def get_id(self):
          return self.id
          
     
class Frontier:
     def __init__(self):
          self.frontier = []
     
     def pop(self):
          '''Retrieves element from the data strcuture'''
          
          return self.frontier.pop()
     
     def push(self, element):
          '''Adds an element to the data structure'''
          
          self.frontier.append(element)
          
     def __bool__(self):
          if len(self.frontier)>0:
               return True
          return False
     
# For  Breadth-First Search
class QueueFrontier(Frontier):
     def __init__(self):
          super().__init__()
          
     def pop(self):
          return self.frontier.pop(0)
     
     def push(self, element):
          return super().push(element)
     
# For Depth-First Search
class StackFrontier(Frontier):
     def __init__(self):
          super().__init__()
          
     def pop(self):
          return super().pop()
     
     def push(self, element):
          return super().push(element)
     
def actions(state:State):
     # TODO
     pass

def result(state, action)->State:
     # TODO
     pass

     
def search(source:int, target:int):
     initial_state = State(
          parent=None,
          name=get_name_for(source)
     )
     
     solutions = []
     frontier = QueueFrontier()
     frontier.push(initial_state)
     while frontier:
          state:State = frontier.pop()
          if state.get_id==target:
               solutions.append(state)
          
               
          
     
             
def shortest_path(source:int, target:int):
     pass
            
print(movies)
print(people)
print(stars)
print(get_name_for(129))

          