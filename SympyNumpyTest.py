#                    SYMPY REVISION FINAL TASK

#                              TASK 1
"""
from sympy import symbols,diff,integrate,solve,lambdify
X=symbols("X")           # DEFINED SYMBOLS 
W=5                              # KN/m
M_expr=W*(X**2)/2
M_derivative=diff(M_expr,X)
M_integration=integrate(M_expr,X)
soln_4=solve(M_expr - 10,X)          # SOLVE FOR X WHEN M = 10 KNM
func=lambdify((X),M_expr)            # lambdify function for M expression
soln_5=func(3)                       # AT X = 3M 
print(f"The derivative of M : {M_derivative}")
print(f"The integration of M : {M_integration}")
print(f"Solution 4 : {soln_4}")
print(f"Solution 5 : {soln_5}")
"""

#                              TASK 2
"""
from sympy import symbols,Piecewise,solve
L=8
P1=10                      # 10 KN AT X = 2
P2=15                      # 15 KN AT X=6
X=symbols("X")
M=Piecewise(               # Piecewise(expr,condition)
    (0,X<2),
    (P1*(X-2),(X>=2) & (X<6)),
    (P1*(X-2) + P2*(X-6),(X>=6) & (X<=8))
)
soln_4=solve(M - 20 , X)
print(f"The moment formula we used : {M}")
print(f"SOlution 4 : {soln_4}")
"""

#                            NUMPY REVISION FINAL TASK 

#                                 TASK 1 
"""
import numpy as np 
points=np.linspace(0,10,11)
W=6                              # 6 KN/M
M=np.zeros(len(points))
M=W*(points**2)/2
print(f"Minimum Bending moment : {M.min()} KNM")
print(f"Maximum Bending Moment  : {M.max()} KNM")
print(f"Mean Of bending moment  : {M.mean()} KNM")
print(f"Sum Of Bending Moment   : {M.sum()} KNM")
"""

#                                  TASK 2 
"""
import numpy as np
X=np.linspace(0,10,11)
W=5                                  # 5 KN/M
W_array=np.ones(len(X))*W
M=W_array*(X**2)/2
safety=np.zeros(len(X))
safety[M > 30] = 1              # 1 means dangerous and 0 means safe 
print(f"Bending Moments : {M} KNM")
print(f"Safety          : {safety}")
print("1 means dangerous.\n0 means safe.")
"""