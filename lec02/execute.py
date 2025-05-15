# from itertools import product

# cartesian = product([True, False], repeat=3)

# for t in cartesian:
#      print(dict(zip(['P','Q','R'], t)))
     
     

from model import LogicalInferenceEngine
from logic import And, Symbol, Implication, Not

P = Symbol("It is raining")
Q = Symbol("Jack goes out")
R = Symbol("It is a Tuesday")

e = LogicalInferenceEngine(And(
     Implication(And(R, Not(P)), Q),    # If it is a tuesday and it does not rain implies that Jack goes out
     Not(Q),                            # Jack does not go out
     R                                  # It is a Tuesday
))
s = e.evaluate_for(P)                   
print(s)