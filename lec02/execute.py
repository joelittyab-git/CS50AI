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
     Implication(And(R, Not(P)), Q),
     Not(Q),
     R    #P should return true
))
s = e.evaluate_for(P)
print(s)