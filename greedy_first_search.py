from copy import deepcopy
import math


class Action:
     RIGHT = 1
     LEFT = 2
     TOP = 3
     BOTTOM = 4
     
class Element:
     WALL = 'X'
     PATH = ' '
     AGENT = ':'
     GOAL = 'G'

class State:
     def __init__(self, parent, board:list[list], action:Action):
          self.board = deepcopy(board)
          self.parent = parent
          self.action = action
          self.heurestic = self.generate_heurestic()
          
     # Returns the 2-d index of the agent
     def get_pos(self, delimeter = Element.AGENT)-> tuple:
          assert len(self.board)>0
          
          rows = len(self.board)
          columns = len(self.board[0])
          
          for i in range(rows):
               for j in range(columns):
                    if self.board[i][j] == delimeter:
                         return i,j
          raise Exception("No Agent found")
          
     def get_parent(self):
          return self.parent
     
     def get_board(self):
          return deepcopy(self.board)
     
     def generate_heurestic(self):
          try:
               a,b = self.get_pos()
               i,j = self.get_pos(delimeter=Element.GOAL)
          except:
               return 0
          else:
               h = abs(i-a)
               w = abs(b-j)
          
               return h+w
     
     def __str__(self):
          string = ''
          for i in self.board:
               string+=str(i)+'\n'
          return string

def generate_goal_board(initial:State):
     i,j = initial.get_pos(delimeter=Element.GOAL)
     a,b = initial.get_pos()
     board = deepcopy(initial.board)
     
     # Places the agent at goal and resets the agent position at start with a path
     board[i][j] = Element.AGENT
     board[a][b] = Element.PATH
     
     return board     

def get_action(state:State):
     actions = []
     
     x,y = state.get_pos()
     if state.board[x][y+1] == Element.PATH or state.board[x][y+1] == Element.GOAL:
          actions.append(Action.RIGHT)
     if state.board[x][y-1] == Element.PATH or state.board[x][y-1] == Element.GOAL:
          actions.append(Action.LEFT)
     if state.board[x-1][y] == Element.PATH or state.board[x-1][y] == Element.GOAL:
          actions.append(Action.TOP)
     if state.board[x+1][y] == Element.PATH or state.board[x+1][y] == Element.GOAL:
          actions.append(Action.BOTTOM)
          
     return actions
          
def result(state:State, action:Action)->State:
     board = deepcopy(state.board)
     a,b = state.get_pos()
     board[a][b] = Element.PATH
     
     if action == Action.RIGHT:
          board[a][b+1] = Element.AGENT
     elif action == Action.LEFT:
          board[a][b-1] = Element.AGENT
     elif action == Action.TOP:
          board[a-1][b] = Element.AGENT
     elif action == Action.BOTTOM:
          board[a+1][b] = Element.AGENT
     
     return State(
          parent=state,
          board=board,
          action=action
     )

def search(initial:State):
     frontier = [initial]
     explored = []
     
     goal_pos = initial.get_pos(Element.GOAL)
     
     
     while frontier:
          top = frontier[0]          
          
          for i in frontier:
               if i.heurestic<top.heurestic: top = i
          frontier.remove(top)
          print(top)
          explored.append(str(top.board))
          
          if top.get_pos()==goal_pos:
               print("Found")
               break

     
               
          actions = get_action(top)
          for action in actions:
               r = result(top, action=action)
               if any(str(r.board) == str(exp_board) for exp_board in explored):
                    continue
               else:
                    frontier.append(r)


maze = [
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
     ['X', ':', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
     ['X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'X', ' ', ' ', ' ', 'X'],
     ['X', ' ', 'X', 'X', ' ', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
     ['X', ' ', 'X', 'X', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
     ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', ' ', ' ', 'X', 'X', 'X'],
     ['X', 'X', ' ', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'G', 'X'],
     ['X', 'X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', ' ', 'X'],
     ['X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]


# def traverse(child:State):
#      print("Traversing: ")
#      node = child
#      if node.parent is None:
#           print("Nothing to traverse")
#           return
#      board = deepcopy(node.board)
#      while node is not None:
#           a,b = node.get_pos()
#           board[a][b] = Element.AGENT
#           node = node.parent
     
#      for i in board:
#           print(i)
#      print(f"COST: {child.cost}")

     

i_state = State(
     parent=None,
     board=maze,
     action=None
)

search(i_state)