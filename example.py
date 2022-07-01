from numpy import *
import openturns as ot
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import scipy as sp
import openturns.viewer
import openturns.viewer as viewer
sps=sp.special
import login.py

# an example code to add to github

y=4

x=y**2+1

q=x+y

k=q*x*y

login.py