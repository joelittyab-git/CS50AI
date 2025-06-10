from vector import Vector2D, Vec
from kdtree import Node, BinaryTree2D,traverse
import csv



data = list()

def load_csv():
     """
     Loads csv data
     """
     global data
     
     with open("Learning\\res\\perceptron_regression_dataset.csv", "r") as file:
          reader = csv.reader(file)
          reader = list(reader)
          reader.pop(0)
          # for read in reader:
          #      print(read)
               
          data = reader

load_csv()

def plot_data():
     """Plots loaded data"""
     vectors = list()

     for x1,x2, y in data:
          if int(float(y))==1:
               classifier = 'A'
          else:
               classifier = 'B'
          vector = Vector2D(float(x1), float(x2),name=classifier)
          vectors.append(vector)
          
     return BinaryTree2D(vectors).construct()


def classify(k, vector:Vec):
     """Classifies a point based on k neighbouring points"""
     node = plot_data()
     points  = traverse(node, vector,k)
     print("Points: \n",points)
     for _, vector in points:
          print(vector.name)
     
     classA = 0
     classB = 0

     for _,vector in points:
          assert isinstance(vector, Vector2D)
          print(vector.name)
          if vector.name=='A':
               classA+=1
          else: 
               classB+=1

     if classA>classB:
          print("A")
     else :
          print("B")
     
classify(3,Vector2D(0,0))