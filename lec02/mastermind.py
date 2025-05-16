from logic import (
     Not,
     Symbol,
     Or,
     Implication,
     And
)

from model import LogicalInferenceEngine


colours = ['Red', 'Green', 'Blue', 'Yellow']
symbols = []
knowledge = []

for i in range(len(colours)):
     i_knowledge = []
     for colour in colours:
          symbols.append(Symbol(f"{colour}-{i+1}"))          


for i in range(len(colours)):
     inner = []
     for t in colours:
          inner.append(Symbol(f"{t}-{i+1}"))
     knowledge.append(Or(*inner))

for i in colours:
     for j in colours:
          for k in range(len(colours)):
               if i!=j:
                    A = Symbol(f'{i}-{k+1}')
                    B = Symbol(f'{j}-{k+1}')
                    implication = Implication(A, Not(B))
                    knowledge.append(implication)
                    
for colour in colours:
     for i in range(len(colours)):
          for j in range(len(colours)):
               if j!=i:
                    A = Symbol(f'{colour}-{i+1}')
                    B = Symbol(f'{colour}-{j+1}')
                    knowledge.append(Implication(A, Not(B)))
     
clue1 = ['Red-1','Blue-2', 'Green-3', 'Yellow-4'] # 2 are correct

OR = []
for i in range(len((clue1))):
     for j in range(i,len((clue1))):
          if i!=j:
               OR.append(And(Symbol(clue1[i]), Symbol(clue1[j])))
knowledge.append(Or(*OR))

clue2 = ['Blue-1','Red-2', 'Green-3', 'Yellow-4'] # None are correct
for i in clue2:
     A = Symbol(i)
     knowledge.append(Not(A))


a = knowledge.pop()
b = knowledge.pop()
propositional_k = And(a,b)

for k in knowledge:
     propositional_k.add(k)
     
e = LogicalInferenceEngine(propositional_k)


'''
(¬(Yellow-4) ∧ ¬(Green-3) ∧
(Red-1 ∨ Green-1 ∨ Blue-1 ∨ Yellow-1) ∧ (Red-2 ∨ Green-2 ∨ Blue-2 ∨ Yellow-2) ∧
(Red-3 ∨ Green-3 ∨ Blue-3 ∨ Yellow-3) ∧ (Red-4 ∨ Green-4 ∨ Blue-4 ∨ Yellow-4) ∧ (Red-1 => ¬(Green-1)) ∧
(Red-2 => ¬(Green-2)) ∧ (Red-3 => ¬(Green-3)) ∧ (Red-4 => ¬(Green-4)) ∧ (Red-1 => ¬(Blue-1)) ∧ (Red-2 => ¬(Blue-2)) ∧
(Red-3 => ¬(Blue-3)) ∧ (Red-4 => ¬(Blue-4)) ∧ (Red-1 => ¬(Yellow-1)) ∧ (Red-2 => ¬(Yellow-2)) ∧ (Red-3 => ¬(Yellow-3)) ∧ (Red-4 => ¬(Yellow-4)) ∧
(Green-1 => ¬(Red-1)) ∧ (Green-2 => ¬(Red-2)) ∧ (Green-3 => ¬(Red-3)) ∧ (Green-4 => ¬(Red-4)) ∧ (Green-1 => ¬(Blue-1)) ∧ (Green-2 => ¬(Blue-2)) ∧ (Green-3 => ¬(Blue-3)) ∧
(Green-4 => ¬(Blue-4)) ∧ (Green-1 => ¬(Yellow-1)) ∧ (Green-2 => ¬(Yellow-2)) ∧ (Green-3 => ¬(Yellow-3)) ∧ (Green-4 => ¬(Yellow-4)) ∧ (Blue-1 => ¬(Red-1)) ∧ (Blue-2 => ¬(Red-2)) ∧
(Blue-3 => ¬(Red-3)) ∧ (Blue-4 => ¬(Red-4)) ∧ (Blue-1 => ¬(Green-1)) ∧ (Blue-2 => ¬(Green-2)) ∧ (Blue-3 => ¬(Green-3)) ∧ (Blue-4 => ¬(Green-4)) ∧ (Blue-1 => ¬(Yellow-1)) ∧
(Blue-2 => ¬(Yellow-2)) ∧ (Blue-3 => ¬(Yellow-3)) ∧ (Blue-4 => ¬(Yellow-4)) ∧ (Yellow-1 => ¬(Red-1)) ∧ (Yellow-2 => ¬(Red-2)) ∧ (Yellow-3 => ¬(Red-3)) ∧ (Yellow-4 => ¬(Red-4)) ∧
(Yellow-1 => ¬(Green-1)) ∧ (Yellow-2 => ¬(Green-2)) ∧ (Yellow-3 => ¬(Green-3)) ∧ (Yellow-4 => ¬(Green-4)) ∧ (Yellow-1 => ¬(Blue-1)) ∧ (Yellow-2 => ¬(Blue-2)) ∧ (Yellow-3 => ¬(Blue-3)) ∧
(Yellow-4 => ¬(Blue-4)) ∧ (Red-1 => ¬(Red-2)) ∧ (Red-1 => ¬(Red-3)) ∧ (Red-1 => ¬(Red-4)) ∧ (Red-2 => ¬(Red-1)) ∧ (Red-2 => ¬(Red-3)) ∧ (Red-2 => ¬(Red-4)) ∧ (Red-3 => ¬(Red-1)) ∧ (Red-3 => ¬(Red-2)) ∧
(Red-3 => ¬(Red-4)) ∧ (Red-4 => ¬(Red-1)) ∧ (Red-4 => ¬(Red-2)) ∧ (Red-4 => ¬(Red-3)) ∧ (Green-1 => ¬(Green-2)) ∧ (Green-1 => ¬(Green-3)) ∧ (Green-1 => ¬(Green-4)) ∧
(Green-2 => ¬(Green-1)) ∧ (Green-2 => ¬(Green-3)) ∧ (Green-2 => ¬(Green-4)) ∧ (Green-3 => ¬(Green-1)) ∧ (Green-3 => ¬(Green-2)) ∧ (Green-3 => ¬(Green-4)) ∧ (Green-4 => ¬(Green-1)) ∧
(Green-4 => ¬(Green-2)) ∧ (Green-4 => ¬(Green-3)) ∧ (Blue-1 => ¬(Blue-2)) ∧ (Blue-1 => ¬(Blue-3)) ∧ (Blue-1 => ¬(Blue-4)) ∧ (Blue-2 => ¬(Blue-1)) ∧ (Blue-2 => ¬(Blue-3)) ∧ (Blue-2 => ¬(Blue-4)) ∧
(Blue-3 => ¬(Blue-1)) ∧ (Blue-3 => ¬(Blue-2)) ∧ (Blue-3 => ¬(Blue-4)) ∧ (Blue-4 => ¬(Blue-1)) ∧ (Blue-4 => ¬(Blue-2)) ∧ (Blue-4 => ¬(Blue-3)) ∧ (Yellow-1 => ¬(Yellow-2)) ∧ (Yellow-1 => ¬(Yellow-3)) ∧
(Yellow-1 => ¬(Yellow-4)) ∧ (Yellow-2 => ¬(Yellow-1)) ∧ (Yellow-2 => ¬(Yellow-3)) ∧ (Yellow-2 => ¬(Yellow-4)) ∧ (Yellow-3 => ¬(Yellow-1)) ∧ (Yellow-3 => ¬(Yellow-2)) ∧ (Yellow-3 => ¬(Yellow-4)) ∧
(Yellow-4 => ¬(Yellow-1)) ∧ (Yellow-4 => ¬(Yellow-2)) ∧ (Yellow-4 => ¬(Yellow-3)) ∧
((Red-1 ∧ Blue-2) ∨ (Red-1 ∧ Green-3) ∨ (Red-1 ∧ Yellow-4) ∨ (Blue-2 ∧ Green-3) ∨ (Blue-2 ∧ Yellow-4) ∨ (Green-3 ∧ Yellow-4)) ∧ ¬(Blue-1) ∧ ¬(Red-2))
'''
print(propositional_k.formula())
for s in symbols:
     if e.evaluate_for(s):
          print(s)