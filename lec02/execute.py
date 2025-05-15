# from itertools import product

# cartesian = product([True, False], repeat=3)

# for t in cartesian:
#      print(dict(zip(['P','Q','R'], t)))
     
     

'''
If it is a weekday, then Alice goes to work.
If Alice goes to work, then Bob stays home.
If it is not a weekday, then Charlie goes out.
If Bob stays home, then Charlie does not go out.
It is a weekday, and Charlie goes out.
'''

from model import LogicalInferenceEngine
from logic import And, Symbol, Implication, Not

W = Symbol("It is a weekday")
A = Symbol("Alice goes to work")
B = Symbol("Bob stays home")
C = Symbol("Charlie goes out")

knowledge = And(
    Implication(W, A),          # If it's a weekday → Alice works
    Implication(A, B),          # If Alice works → Bob stays home
    Implication(Not(W), C),     # If not a weekday → Charlie goes out
    Implication(B, Not(C)),     # If Bob stays home → Charlie doesn't go out
    W,                          # It is a weekday
    C                           # Charlie goes out
)
query = Not(C)                  

e = LogicalInferenceEngine(knowledge)
s = e.evaluate_for(query)
print(s)