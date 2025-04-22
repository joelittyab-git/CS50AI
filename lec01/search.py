from copy import deepcopy

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
     def __init__(self, parent, board:list[list], cost:int, action:Action):
          self.board = deepcopy(board)
          self.parent = parent
          self.cost = cost
          self.action = action
          
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
     netcost = state.cost+1
     
     return State(
          parent=state,
          board=board,
          cost=netcost,
          action=action
     )


def search(initial_state:State):
     # Contains the all the available nodes of the states
     frontier = [initial_state]
     explored = []
     goal_board = generate_goal_board(initial_state)
     solutions = []
     
     print("Goal: ")     
     for i in goal_board:
          print(i)
     
     while frontier:
          upper = frontier.pop()
          # print(upper)
          # if any([upper.board == board for board in explored]):
          #      continue
          explored.append(deepcopy(upper.board))
          print(upper)
          if upper.board == goal_board:
               # traverse(upper)
               solutions.append(upper)
               print("Finished")
          actions = get_action(upper)
          print(actions)
          
          for action in actions:
               newstate = result(
                    state=upper,
                    action=action
               )
               if newstate.board not in explored:
                    frontier.insert(0,newstate)
     # else:
     #      print("Path not found")
     #      return
     print(solutions)
     for sol in solutions:
          traverse(sol)
          
     print("Path found!!")
          
maze = [
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
     ['X', ':', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
     ['X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'X', ' ', ' ', ' ', 'X'],
     ['X', ' ', 'X', 'X', ' ', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
     ['X', ' ', 'X', 'X', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
     ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X', 'X', 'X', 'X', ' ', ' ', 'X', ' ', 'X'],
     ['X', 'X', ' ', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', 'G', 'X'],
     ['X', 'X', ' ', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', ' ', 'X'],
     ['X', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', 'X'],
     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]


def traverse(child:State):
     print("Traversing: ")
     node = child
     if node.parent is None:
          print("Nothing to traverse")
          return
     board = deepcopy(node.board)
     while node is not None:
          a,b = node.get_pos()
          board[a][b] = Element.AGENT
          node = node.parent
     
     for i in board:
          print(i)
     print(f"COST: {child.cost}")

     

i_state = State(
     parent=None,
     board=maze,
     cost=0,
     action=None
)

search(i_state)
