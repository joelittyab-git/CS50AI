from itertools import product

class Proposition:
     
     def evaluate(self, model):
          '''Evaluates the logical proposition against a model containing values for each data value'''
          
          raise Exception("Nothing to evaluate ('evaluate' function not implemented)")
     
     def formula(self):
          '''Returns the string representation of the logic'''
          
          return ""
     
     def symbols(self):
          '''Returns the various symbols in the currect expression'''
          
          return set()
     
     @staticmethod
     def validate(proposition):
          '''Valdates if an object is a proposition'''
          
          if not isinstance(proposition, Proposition):
               raise TypeError("Must be a logical proposition")
          
          
class Symbol(Proposition):
     def __init__(self, name):
          self.name = name
          
     def __eq__(self, value):
          return isinstance(value, Symbol) and self.name == value.name
     
     def __repr__(self):
          return self.name
     
     def __hash__(self):
          return hash(("symbol", self.name))
          
     def evaluate(self, model:dict):
          try:
               # Checks for the symbol instance as a key in the model dictionary
               return bool(model[self])
          except KeyError:
               raise Exception("No symbol proposition in the provided model")
          
     def formula(self):
          return str(self.name)
     
     def symbols(self)->set:
          return {self.name}
     
     
class Not(Proposition):
     def __init__(self, operand:Proposition):
          Proposition.validate(operand)
          self.operand = operand
     
     def __eq__(self, value):
          return isinstance(value, Not) and self.operand == value.operand
     
     def __hash__(self):
        return hash(("not", hash(self.operand)))
   
     def __repr__(self):
          return f"NOT({self.operand})"
     
     def evaluate(self, model):
          return not self.operand.evaluate(model=model)
     
     def formula(self):
          return f"¬({self.operand.formula()})"
     
     def symbols(self):
          return self.operand.symbols()
     
class And(Proposition):
     def __init__(self, *conj):
          if len(conj) < 2:
               raise Exception("And requires at least two operands.")
          for conjunction in conj:
               Proposition.validate(conjunction)
          self.conjuncts = list(conj)
          
     def __eq__(self, value):
          return isinstance(value, And) and self.conjuncts == value.conjuncts
     
     def __hash__(self):
          return hash(
                    ("and", tuple(hash(conjunct) for conjunct in self.conjuncts))
          )
          
     def __repr__(self):
          string = ", ".join([str(conjunct) for conjunct in self.conjuncts])
          return f"And({string})"
     
     def add(self, conj):
          Proposition.validate(conj)
          self.conjuncts.append(conj)
          
     def evaluate(self, model:dict):
          for conj in self.conjuncts:
               conj:Proposition = conj
               if not conj.evaluate(model=model):
                    return False
          return True
     def formula(self):
          string =  " ∧ ".join([conj.formula() for conj in self.conjuncts])
          return f"({string})"
     
     def symbols(self):
          return set.union(*[conj.symbols() for conj in self.conjuncts])
     
class Or(Proposition):
     def __init__(self, *operands):
          if len(operands)<2:
               raise Exception("Or requires atleast two operands")
          for operand in operands:
               Proposition.validate(operand)
          self.operands = list(operands)
          
     def __eq__(self, value):
          return isinstance(value, Or) and self.operands == value.operands
     
     def __hash__(self):
          return hash(
                    ("or", tuple(hash(disjunct) for disjunct in self.operands))
          )
     def __repr__(self):
          string = ", ".join([str(oper) for oper in self.operands])
          return f"Or({string})"
     
     def add(self, disj):
          Proposition.validate(disj)
          self.operands.append(disj)
          
     def evaluate(self, model):
          for oper in self.operands:
               oper:Proposition = oper
               if oper.evaluate(model=model):return True
          return False
     
     def formula(self):
          string = " v ".join([oper.formula() for oper in self.operands])
          return f"({string})"
     
     def symbols(self):
          return set.union(*[oper.symbols() for oper in self.operands])