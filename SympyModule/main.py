
# CREATE SYMBOLIC VARIABLES 
"""
from sympy import symbols
x=symbols("x")
y=x**2+5
print(y)
"""

# TASK 1 :
"""
from sympy import symbols
F,A=symbols("F A")
S=F/A
print(S)
"""

# DERIVATIVE OF A FUNCTION
"""
from sympy import symbols,diff
x=symbols("x")
y=x**3+5*x+6
dy_dx=diff(y,x) # for second degree > diff(y,x,2)
print(dy_dx)
"""

# Task 2 :
"""
from sympy import symbols,diff
F,A,T=symbols('F A T')
F=T**2   # ASSUME TIME IN MINUTES | FORCE IS INCREASING WITH TIME
A=T**3   # AREA IS INCREASING WITH TIME 
S=F/A    # STRESS FORMULA 
ds_dt=diff(S,T)  # DIFFERENTIATE STRESS WITH REPSPECT TO TIME 
print(ds_dt)
"""

# SOLVING EQUATIONS
"""
from sympy import symbols,Eq,solve
x=symbols("x")
eq1=Eq(x**2+5*x+6,0)  # DEFINE EQUATION WITH SYMBOLS JUST AS RIGHT AND LEFT
sol=solve(eq1,x)      # SOLUTION OF EQUATION FOR VAIABLE X
print(sol)
"""

#TASK 3 :
"""
from sympy import symbols,Eq,solve
F,A,S=symbols("F A S")
eq1=Eq(S,F/A)
eq1=eq1.subs({S:5,A:10})  # SUBSTITUTE VALUE IN EQUATION
sol=solve(eq1,F)  # FIND FORCE WHEN A=10,S=5
print(sol)
"""

#TASK 4:
"""
from sympy import symbols,Eq,solve
F,A=symbols("F A")                   # DEFINE SYMBOLS F AND A BUT NOT S CAUSE S IS EXPRESSION WHICH HOLDS F/A
S=F/A                                # EXPRESSION 
val=S.subs({F:120,A:30})             # AFTER SUBSTITUTION, STORE THE RIGHT EXPRESSION IN val
print(val)
"""


# COMBINED EXERCISE OF ALL TOPICS WE DID AS FAR 
"""
from sympy import symbols,Eq,solve,diff
M,P,L=symbols("M P L")                   #SYMBOLS DEFINED
M_formula=(P*L)/4                        #WRITTEN FORMULA SYMBOLICALLY
M_equation=Eq(M,M_formula)                 # EQUATION DEFINED
dm_dp=diff(M_formula,P)                  # DIFFFERENTIATION OF M WITH REPECT TO P
print(f"The Derivative Of M with repect to P : {dm_dp} ")
qn4_soln=solve(M_equation.subs({M:50,L:10}),P)    # SOLVE FOR P WHEN M=50,L=10
print(f"Solution Of Qn.4, P = {qn4_soln} N/m2")
qn5_soln=M_formula.subs({P:25,L:8})                # SUBSTITUTE THE VALUE AND GET THE OUTPUT OF M
print(f"Solution Of Qn.5 , M = {qn5_soln} Nm")
"""










