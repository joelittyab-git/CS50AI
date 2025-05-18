import csv
from dotenv import load_dotenv
import os
from copy import deepcopy

load_dotenv()

movies = {}
people = {}
stars = []

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
               stars.append(read)
          
load_file_data()

def get_person_name_for(id:int):
     '''Returns the persons name based on his/her id'''
     return people[str(id)][0]

def get_movie_id_for(id:int):
     '''Returns the movie ids in integers for a given person id'''
     movies = []
     for t in stars:
          if str(id).strip()==t[0].strip():
               movies.append(int(t[1]))
     return movies
               
def get_stars_for(id:int):
     '''Returns all the stars (person id) for the movie with id "id"'''
     movie_stars = []
     for t in stars:
          if t[1]==str(id):
               movie_stars.append(int(t[0]))
               
     return movie_stars

# AI impl. ----------------
class State:
     def __init__(self,parent, name:str, cost:int, action, id):
          assert type(id)==int
          
          self.parent = parent     # Parent state
          self.name = name 
          self.cost = cost
          self.action = action
          self.id = id
          
     def __str__(self):
          return f"{self.name} | {self.id}"
          
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
     
     def push(self, *elements):
          '''Adds an element to the data structure'''
          for element in elements:
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
     
     def push(self, *elements):
          return super().push(*elements)
     
# For Depth-First Search
class StackFrontier(Frontier):
     def __init__(self):
          super().__init__()
          
     def pop(self):
          return super().pop()
     
     def push(self, *elements):
          return super().push(*elements)
     
def actions(state:State)->list:
     p_id = int(state.get_id())
     return get_movie_id_for(p_id)

# Debug
def result(preceeding_state:State, action:int)->list[State]:
     results = []
     
     # Get all the actors in the new movie
     for star in get_stars_for(action):
          name = get_person_name_for(star)
          cost = preceeding_state.get_cost()+1
          new_state = State(
               parent=preceeding_state,
               name=name,
               cost=cost,
               action=action, 
               id=star
          )
          results.append(new_state)
     return results

     
def search(source:int, target:int):
     initial_state = State(
          parent=None,
          name=get_person_name_for(source),
          cost=0,
          id=source,
          action=None
     )
     
     solutions = []
     visited = []
     frontier = QueueFrontier()
     frontier.push(initial_state)
     while bool(frontier):
          state:State = frontier.pop()
          print(state)
          if state.get_id() in visited:
               continue
          visited.append(state.get_id())
          if state.get_id()==target:
               solutions.append(state)
               print(f"COST: {state.get_cost()}")
               traverse(state)
               break
          all = actions(state=state)
          for action in all:
               new_states:list = result(preceeding_state=state, action=action)
               print(f"New states: {new_states}")
               frontier.push(*new_states)
               

def traverse(state:State, k = 0):
     if state.parent is None:
          print(f" [{state}]")
          return
     
     if k==0:
          print(f"[{state}] --> ({state.action})", end='')
          return traverse(state=state.parent, k = 1)
     
     print(f" --> [{state}] --> ({state.action})", end='')
     return traverse(state=state.parent, k=k)
     
               
          
search(102,144)
             

          