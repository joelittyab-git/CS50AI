from vector import Vector3D, Vec
from kdtree import Node, BinaryTree2D
import csv



data = list()

def load_csv():
     """
     Loads csv data
     """
     global data
     
     with open("res\\perceptron_regression_dataset.csv", "r") as file:
          reader = csv.reader(file)
          reader = list(reader)
          reader.pop(0)
          # for read in reader:
          #      print(read)
               
          data = reader

load_csv()

def plot_data():
     for x1,x2,y in data:
          BinaryTree2D()

def classify(k, vector:Vec):
     pass