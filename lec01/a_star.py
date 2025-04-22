from copy import deepcopy

'''
a = g(n1) + h(x1,y1)
b = g(n2) + h(x2,y2)

net = min(a,b)

g: net steps taken
h: heurestic (Manhattan distance)
'''

class Element:
     WALL = 'X'
     PATH = ' '
     AGENT = ':'
     GOAL = 'G'

class Action:
     RIGHT = 1
     LEFT = 2
     TOP = 3
     BOTTOM = 4
     
class State:
     def __init__(self, board:list, parent, action:Action):
          self.board = board
          self.parent:State = parent
          self.action = action
          self.g = self.calculate_steps_taken()
          self.h = self.calculate_heurestic()
          self.eval_fn = self.evaluate_function()
          
     # Calculates g(n): The total number of steps taken
     def calculate_steps_taken(self):
          if self.parent == None:
               return 0
          return self.parent.get_g() + 1
     
     def calculate_heurestic(self):
          # Calculation of heurestic
          agent_x, agent_y = self.get_pos()
          try:
               goal_x,goal_y = self.get_pos(deli = Element.GOAL)
               h_x = abs(agent_x-goal_x)
               h_y = abs(agent_y-goal_y)
          except:
               return 0          
          return h_x + h_y
     
     def get_pos(self, deli:Element = Element.AGENT):
          assert len(self.board)>0
          
          rows = len(self.board)
          columns = len(self.board[0])
          
          for i in range(rows):
               for j in range(columns):
                    if self.board[i][j] == deli:
                         return i,j
          if Element.GOAL==deli:
               raise Exception("No Goal found")
               return
          raise Exception("No agent found")          
     
     # Evaluates g(n) + h(x,y) : evalueation function
     def evaluate_function(self):
          g = self.get_g()
          h = self.get_h()
          
          return g + h
          
          
     def get_g(self):
          return self.g
     
     def get_h(self):
          return self.h
     
     def __str__(self):
          string = ""
          for i in self.board:
               string+=str(i)+"\n"
          return string
     
class AStarFrontier:
     def __init__(self, initial_state:State = None):
          if initial_state is None:
               self.array = []
               return
          self.array = [initial_state]
     
     def __bool__(self):
          if len(self.array)==0:
               return False
          return True
          
     def push(self, element:State):
          n = len(self.array)
          
          if n==0:
               self.array.append(element)
               return
          
          for i in range(n):
               arr:State = self.array[i]
               if element.eval_fn<arr.eval_fn:
                    self.array.insert(i, element)
                    break
          else: 
               self.array.append(element)
               
     def pop(self):
          return self.array.pop(0)
     
     
class Search:
     
     def __init__(self, board):
          self.initial_board = board
          self.initial_state = State(
               board=self.initial_board,
               parent=None,
               action=None
          )
          self.frontier = AStarFrontier(self.initial_state)    
          self.goal_board = self.generate_goal_state()
          
     def generate_goal_state(self):
          agent_x,agent_y = self.initial_state.get_pos()
          goal_x,goal_y = self.initial_state.get_pos(deli=Element.GOAL)
          
          c_board = deepcopy(self.initial_board)
          c_board[agent_x][agent_y] = Element.PATH
          c_board[goal_x][goal_y] = Element.AGENT
          
          return c_board
          
          
     def action(self, state:State):
          agent_x,agent_y = state.get_pos()
          actions = []
          
          if state.board[agent_x][agent_y+1]==Element.PATH or state.board[agent_x][agent_y+1]==Element.GOAL :
               actions.append(Action.RIGHT)
          if state.board[agent_x][agent_y-1]==Element.PATH or state.board[agent_x][agent_y-1]==Element.GOAL :
               actions.append(Action.LEFT)
          if state.board[agent_x-1][agent_y]==Element.PATH or state.board[agent_x-1][agent_y]==Element.GOAL :
               actions.append(Action.TOP)
          if state.board[agent_x+1][agent_y]==Element.PATH or state.board[agent_x+1][agent_y]==Element.GOAL :
               actions.append(Action.BOTTOM)
               
          return actions
     
     def result(self, state:State, action:Action):
          agent_x,agent_y = state.get_pos()
          c_board = deepcopy(state.board)
          
          # Reseting the board elements
          c_board[agent_x][agent_y] = Element.PATH
          
          if action==Action.RIGHT:
               c_board[agent_x][agent_y+1] = Element.AGENT
          elif action==Action.LEFT:
               c_board[agent_x][agent_y-1] = Element.AGENT
          elif action==Action.TOP:
               c_board[agent_x-1][agent_y] = Element.AGENT
          elif action==Action.BOTTOM:
               c_board[agent_x+1][agent_y] = Element.AGENT
               
          return State(
               board=c_board,
               parent=state,
               action=action
          )

     def search(self):
          explored_boards = []
          
          while self.frontier:
               top_state:State = self.frontier.pop()
               print(top_state)
               explored_boards.append(top_state.board)
               # print(self.initial_state)
               print(self.initial_state.get_pos(deli=Element.GOAL), self.initial_state.get_pos())
               if top_state.get_pos()==self.initial_state.get_pos(deli=Element.GOAL):
                    print("Found")
                    break
               
               actions = self.action(top_state)
               for action in actions:
                    state:State = self.result(top_state, action)
                    if not(any([state.board == explored_board for explored_board in explored_boards])):
                         self.frontier.push(state)
                         
          else:
               print("No Solutions found")
                    
               
               
maze = [
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
     ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', 'X'],
     ['X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X'],
     ['X', 'X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
     ['X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
     ['X', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
     ['X', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X'],
     ['X', ':', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

Search(maze).search()
