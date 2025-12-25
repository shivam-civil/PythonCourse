#                                 PANDAS MODULE  

#                         CREATING A DATAFRAME 
"""
import pandas as pd 
data={
    "Beam":["B1","B2","B3"],
    "Span":[4.0,5.5,6.0],
    "Load":[20,30,35]
}
df=pd.DataFrame(data)
print(df)
"""
#                          READING A CSV FILE 
"""
import pandas as pd
df=pd.read_csv("data.csv")
print(df)
"""

#                             ACCESSING DATAS
"""
import pandas as pd
import streamlit as st 
df=pd.read_csv("data.csv")
print(df["Name"])              # ACCESS NAME COLUMN WITH PRIMARY KEY
print(df.loc[0])               # ACCESS 1ST ROW AS DICTIONARY WITH HEADERS 
print(df.loc[0,"Maths"])       # ACCESS MATH MARK OF FIRST ROW (INDEX METHOD) (NOT RECOMMENDED )
print(df.loc[df["Beam"]=="B2","Load"])   # RECOMMENDED ACCESS METHOD 
"""
#   CREATE A NEW COLUMN INSIDE A DATAFRAME BY MULTIPLING ANOTHER COLUMN BY 1.5(VECTORIZED )
"""
import pandas as pd
data={
    "Beam":["B1","B2","B3"],
    "Span":[4.0,5.5,6.0],
    "Load":[20,30,35]
}
df=pd.DataFrame(data)
df["NewColumn"]=5*df["Span"]          # VECTORIZED CALCULATIONS 
print(df)
"""



