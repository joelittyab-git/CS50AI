from linaris.geometry.line import Line2D
from cprint import cprint
import sympy as sp
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

def regress(learning_rate = 0.001, max_epoch = 10000, tol = 1e-8):
     """Linear regression by gradient descent of a learning rate 'β', slope 'm' and intercept 'c'"""
     
     '''Hypothesis line having the equation:
     >>> y = 0'''
     regression_line = Line2D(0,0, name="Y")
     
     """Creating differential symbols"""
     m,c = sp.symbols('m c')
     
     for epoch in range(max_epoch):
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
          dS_dm_val = dS_dm.subs({m:regression_line.slope, c:regression_line.intercept}).evalf()
          dS_dc_val = dS_dc.subs({m:regression_line.slope, c:regression_line.intercept}).evalf()
          
          """Calculates the change in intercept  and slope: 
          >>> Δm = (∂S/∂m)β
          >>> Δc = (∂S/∂c)β
          """
          del_m = dS_dm_val*learning_rate
          del_c = dS_dc_val*learning_rate
          
          if abs(del_m) < abs(tol) and abs(del_c) < abs(tol):
               cprint.ok(f"Converged at epoch {epoch}\nEpoch {epoch}: Slope = {regression_line.slope:.4f}, Intercept = {regression_line.intercept:.4f}")
               break
          
          """Updates the value of slope and intercept":
          >>> m` = m - Δm
          >>> c` = c - Δc
          """
          m_prime = regression_line.slope - del_m
          c_prime = regression_line.intercept - del_c  
          regression_line.set_slope(m_prime)
          regression_line.set_intercept(c_prime)
          
          # log
          if epoch % 100 == 0:
               loss = sum([(float(point['y']) - (regression_line.slope * float(point['x']) + regression_line.intercept))**2 for point in repo])
               cprint.warn(f"Epoch {epoch}: Slope = {regression_line.slope:.4f}, Intercept = {regression_line.intercept:.4f}, Loss = {loss:.4f}")


          
regress()