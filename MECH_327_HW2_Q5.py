# ---------------------------------------- #
# MECH_327_HW2_Q5 [Python File]
# Written By: Thomas Bement
# Created On: 2021-09-30
# 
# Write a computer script to evaluate the specific heat capacity of 
# Carbon Dioxide (CO2) using the polynomials listed in table A.6.  
# Carbon dioxide CO2, c0: 0.45, c1: 1.67, c2: −1.27, c3: 0.39
# 
# Using this script,
# (a)   Find the specific heat capacity at a constant pressure (cp) and at a constant volume 
#       (cv) at 298 K and compare these to tabulated values.
# (b)   Find the specific heat capacity at 500 K and 1200 K. Comment on the trend that you observe.
# (c)   Modify your script to find the change in enthalpy for Carbon Dioxide between 300 K and 500 K.
# (d)   Calculate the enthalpy change between 300 K and 500 K assuming a constant cp.
# (e)   Compare the enthalpy change calculated using your script, the constant cp assumption, 
#       and tabulated values. Comment on which you believe to be the most accurate
#
# ---------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

def Cp_poly(temp, c0, c1, c2, c3):
    t = temp/1000
    return c0 + c1*t + c2*(t**2) + c3*(t**3)

"""
GLOBALS
"""
coeff_lis = [0.45, 1.67, -1.27, 0.39]

"""
QUESTION 5A
"""
Cp_1 = Cp_poly(298, *coeff_lis)
print('Question 5A:')
print('Cp Poly: %.4f [kJ/kg*K]' %(Cp_1))
print('Cp Table: %.4f [kJ/kg*K]' %(0.842)) # Find number from table still
print('----------------------------\n')

"""
QUESTION 5B
"""
t_range = np.linspace(500, 1200, 25)
Cp_range = Cp_poly(t_range, *coeff_lis)
plt.plot(t_range, Cp_range)
plt.title('Trend for Cp vs. Temprature')
plt.xlabel('Temprature [K]')
plt.ylabel('Cp [kJ/kg*K]')
plt.show()
plt.close()
print('Question 5B:')
print('Temp: %.4f [K], Cp Poly: %.4f [kJ/kg*K]' %(t_range[0], Cp_range[0]))
print('Temp: %.4f [K], Cp Poly: %.4f [kJ/kg*K]' %(t_range[-1], Cp_range[-1]))
print('----------------------------\n')

"""
QUESTION 5C
"""
# ∆h = int(Cp*dT)
dT = 0.1 # Step size
t_range = np.arange(300, 500, dT)
dh = 0
for i in range(len(t_range)):
    dh += dT*Cp_poly(t_range[i], *coeff_lis)
print('Question 5C:')
print('∆h Poly: %.4f [kJ/kg]' %(dh))
print('----------------------------\n')

"""
QUESTION 5D
"""
print('Question 5D:')
print('∆h Const: %.4f [kJ/kg]' %(0.842*(500-300)))
print('----------------------------\n')

"""
QUESTION 5E
"""
print('Question 5E:')
print('∆h Tab: %.4f [kJ/kg]' %(401.52-214.38))
print('----------------------------\n')