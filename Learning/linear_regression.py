from linaris.geometry.line import Line2D
import sympy as sp
import math
import csv

repo = list()
def load_csv(csvfile):
     """
     Loads csv data
     """
     global repo
     
     with open(csvfile, 'r', newline='') as file:
          reader = csv.reader(file)  
          next(reader, None)
          repo = list()
          repo = [{'x':read[0], 'y':read[1]} for read in reader]
     
load_csv("Learning/res/noisy_linear_data.csv")

def regress(learning_rate = 0.01, max_epoch = 1000):
     """Linear regression by gradient descent of a learning rate 'β', slope 'm' and intercept 'c'"""
     
     '''Hypothesis line having the equation:
     >>> y = x'''
     hypothesis = Line2D(0,0, name="Y")
     
     """Creating differential symbols"""
     m,c = sp.symbols('m c')
     
     for _ in range(max_epoch):
          """
          Summing up the residuals of the line wrt to each point
          >>> S(c, m) = Σ (yᵢ - (c + m * xᵢ))² [for i = 1 to n]  
          """
          S = sum([(float(point['y']) - (m*float(point['x']) + c))**2 for point in repo])
          """
          ∇S = <∂S/∂m,∂S/∂c>
          Gradient to find the stepest descent and move in that direction to find the minima of the cost function S(c, m)
          """
          dS_dm = sp.diff(S,m)
          dS_dc = sp.diff(S,c)
          
          # print(dS_dc)
          # print(dS_dm)
          
          # substituting values in the derived equation
          dS_dm_val = dS_dm.subs({m:hypothesis.slope, c:hypothesis.intercept}).evalf()
          dS_dc_val = dS_dc.subs({m:hypothesis.slope, c:hypothesis.intercept}).evalf()
          
regress()