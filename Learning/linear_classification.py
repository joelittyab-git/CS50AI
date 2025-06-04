from vector import Vector3D
import csv

data = list()

def load_csv():
     global data
     
     with open("res\\perceptron_regression_dataset.csv", "r") as file:
          reader = csv.reader(file)
          reader = list(reader)
          reader.pop(0)
          # for read in reader:
          #      print(read)
               
          data = reader

load_csv()

'''
              |- 1; W̅.x̄ >=0
ŷ = hᵥᵥ(x) =  |
              |- 0; otherwise

W̅.x̄ = ΣwᵢXᵢ {i=0, x=bias}

Preceptron Rule: 
wᵢ <- wᵢ + η(Δy)xᵢ
Δy = y - ŷ (difference of actual value and assumed value)
'''               
def classify(learning_rate = 0.1, initial_weight = Vector3D(0,0,0), max_epoch=100):
     """
     Finds the weights for the given classified dataset linearly for a linearly separable dataset
     """
     weight = initial_weight     # initial weights
     l_rate = learning_rate   # η
          
     for epoch in range(max_epoch):
          errors = 0
          for x_1,x_2,target in data:
               vec_x = Vector3D(1,float(x_1),float(x_2))        # x̄ : <1,x₁,x₂>
               calculated = vec_x.dot(weight)     # W̅.x̄

               y_predicted = 1 if calculated>=0 else 0
               delta = float(target) - y_predicted  # Δy = y - ŷ          
               if delta==0:continue    # Δy = 0
               
               errors+=1
               weight.set_x(weight.x + l_rate*delta*vec_x.x)
               weight.set_y(weight.y + l_rate*delta*vec_x.y)
               weight.set_z(weight.z + l_rate*delta*vec_x.z)
                    
          print(f"Errors: {errors} Weights: {weight} Epoch: {epoch+1}")
          
          if errors==0:
               break
          
classify()