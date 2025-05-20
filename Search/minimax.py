from copy import deepcopy

'''
_|_|_
_|_|_
 | |
 
00 01 02
10 11 12
20 21 22

['N', 'N', 'N']
['N', 'N', 'N']
['N', 'N', 'N']
'''

class Element:
     X = 'X'
     O = 'O'
     NONE = 'N'
     
     @staticmethod
     def parse(char:str):
          if char==Element.X:
               return Element.X
          elif char==Element.O:    
               return Element.O
          elif char==Element.NONE:
               return Element.NONE
          raise Exception("Invalid Element")
          
     
# class Action:
#      TL = '00'
#      TM = '01'
#      TR = '02'
#      CL = '10'
#      CM = '11'
#      CR = '12'
#      BL = '20'
#      BM = '21'
#      BR = '22'
     
#      def action(a:int, b:int):
#           if a==0 and b

class State:
     def __init__(self, board:list):
          self.board = board
          
     def __str__(self):
          string = ''
          for i in self.board:
               string += "| "
               for j in i:
                    if j!=Element.NONE:
                         string+=str(j) + " | "
                    else:
                         string+="  | "
               string+='\n'
          return string
          
def player(state:State):
     n_o = 0
     n_x = 0
     for i in state.board:
          for j in i:
               if j==Element.O:n_o+=1
               elif j==Element.X:n_x+=1
               
     if n_o==n_x: 
          return Element.X
     return Element.O

def terminal(state:State):
     for i in state.board:
          for j in i:
               if j==Element.NONE:
                    return False
     return True

def results(state:State, element:Element)->list[State]:
     results_list = []
     
     for i in range(len(state.board)):
          for j in range(len(state.board[0])):
               if state.board[i][j] == Element.NONE:
                    copied = deepcopy(state.board)
                    copied[i][j] = element
                    newstate = State(copied)
                    results_list.append(newstate)
                    
     return results_list

def terminal(state:State):
     for i in range(3):
          # checks horizontal blocks
          if state.board[i][0] == state.board[i][1] == state.board[i][2] != Element.NONE: 
               return True
          # checks vertical blocks
          if state.board[0][i] == state.board[1][i] == state.board[2][i] != Element.NONE: 
               return True
          
     if state.board[0][0]==state.board[1][1]==state.board[2][2] != Element.NONE:
          return True
          
     if state.board[0][2]==state.board[1][1]==state.board[2][0] != Element.NONE:
          return True
     
     for i in state.board:
          for j in i:
               if j==Element.NONE:
                    return False
               
     return True

def evaluate(element:Element):
     if element is None:
          return 0
     if element==Element.O:
          return -1
     if element==Element.X:
          return 1 
     else: return 0

def utility(state:State):
     for i in range(3):
          # checks horizontal blocks
          if state.board[i][0] == state.board[i][1] == state.board[i][2] != Element.NONE: 
               return evaluate(Element.parse(state.board[i][0]))
          # checks vertical blocks
          if state.board[0][i] == state.board[1][i] == state.board[2][i] != Element.NONE: 
               return evaluate(Element.parse(state.board[0][i]))
          
     if state.board[0][0]==state.board[1][1]==state.board[2][2] != Element.NONE:
          return evaluate(Element.parse(state.board[0][0]))
          
     if state.board[0][2]==state.board[1][1]==state.board[2][0] != Element.NONE:
          return evaluate(Element.parse(state.board[0][2]))
     
     return 0  #draw
     

          

def max_value(state:State):     
     if terminal(state):
          return utility(state)
     
     v = -2
     for i in results(state=state, element=Element.X):
          min = min_value(state=i)
          if min>v:
               v = min
               
     return v 
          
     

def min_value(state:State):
     if terminal(state):
          return utility(state)
     
     v = 2
     for i in results(state=state, element=Element.O):
          max = max_value(state=i)
          if max<v:
               v = max
     return v  


def input_index():
     inp = input("Enter your index: ")
     i = int(inp[0])
     j = int(inp[1])
     if (i>=0 and i<=2) and (j>=0 and j<=2):
          return i,j
     print("Enter valid number")
     return  input_index()

def first_play(state:State):
    i,j = input_index()
    board = deepcopy(state.board)
    board[i][j] = Element.X
    
    return State(board=board)
    

def start():
     
     initial = State(
          board=[
               [Element.NONE,Element.NONE,Element.NONE],
               [Element.NONE,Element.NONE,Element.NONE],
               [Element.NONE,Element.NONE,Element.NONE]
          ]
     )
     
     state = first_play(initial)
     print(state.board)
     while True:
          
          if terminal(state):
               print("Game Over")
               val = utility(state)
               if val == 1:
                    print("X wins!")
               elif val == -1:
                    print("O wins!")
               else:
                    print("It's a draw!")
               break
          currect = player(state=state)
          if currect==Element.O:
               states = results(state=state, element=Element.O)
               beststate:State = states[0]
               bestval = 2
               for i_state in states:
                    val = max_value(i_state)
                    if val<bestval:
                         bestval = val
                         beststate = i_state
               state = beststate
          elif currect==Element.X:
               i,j = input_index()
               if state.board[i][j]!=Element.NONE:
                    print("Enter valid index")
                    continue
               newboard = deepcopy(state.board)
               newboard[i][j] = Element.X
               newstate = State(newboard)
               state = newstate
          print(state)
          
          
start()