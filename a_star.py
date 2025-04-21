'''
a = g(n1) + h(x1,y1)
b = g(n2) + h(x2,y2)

net = min(a,b)

g: net steps taken
h: heurestic (Manhatten distance)
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
          goal_x,goal_y = self.get_pos(deli = Element.GOAL)
          
          h_x = abs(agent_x-goal_x)
          h_y = abs(agent_y-goal_y)
          
          return h_x + h_y
     
     def get_pos(self, deli:Element = Element.AGENT):
          assert len(self.board)>0
          
          rows = len(self.board)
          columns = len(self.board[0])
          
          for i in range(rows):
               for j in range(columns):
                    if self.board[i][j] == deli:
                         return i,j
          raise Exception("No Agent found")
     
     # Evaluates g(n) + h(x,y) : evalueation function
     def evaluate_function(self):
          g = self.get_g()
          h = self.get_h()
          
          return g + h
          
          
     def get_g(self):
          return self.g
     
     def get_h(self):
          return self.h
          

