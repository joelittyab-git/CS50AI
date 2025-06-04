from vector import Vector3D, Vec
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


def classify(k, vector:Vec):
     pass