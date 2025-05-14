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
          for conjuction in conj:
               Proposition.validate(conjuction)     
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
          Proposition.evaluate(conj)
          self.conjuncts.append(conj)
          
     def evaluate(self, model:dict):
          for conj in self.conjuncts:
               conj:Proposition = conj
               if not conj.evaluate(model=model):
                    return False
          return True