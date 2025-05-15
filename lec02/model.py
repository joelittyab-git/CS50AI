from logic import (
     Symbol,
     Not, 
     Or, 
     And, 
     Implication, 
     Biconditional,
     Proposition
)
from itertools import product

class LogicalInferenceEngine():
     def  __init__(self, knowledge:Proposition):
          Proposition.validate(knowledge)
          self.knowledge_base = knowledge
          
     def evaluate_for(self, query:Proposition):
          
          def evaluate_query(query:Proposition, model):
               return query.evaluate(model)
               
          # creating all possible models of symbols and storing them in model space
          Proposition.validate(query)
          symbols = query.objects().union(self.knowledge_base.objects())
          n_s = len(symbols)
          values = product([True, False], repeat=n_s)
          model_space = []
          for value in values:
               model_space.append(dict(zip(symbols, value)))
               
          
          for model in model_space:
               if self.knowledge_base.evaluate(model=model):
                    if not evaluate_query(query, model):
                         return False
                    
          return True
                    
               
                    
               
          