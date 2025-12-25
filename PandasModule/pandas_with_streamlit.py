#                       PANDAS WITH STREAMLIT 

#                            EXAMPLE 1 
"""
import streamlit as st 
import pandas as pd 
st.title("Axial Stress Calculator")
axial=st.number_input("Axial Load (KN) : ",min_value=0)
area=st.number_input("Area (mm2) : ",min_value=0)
df=pd.DataFrame({
    "Axial_kN":[axial],
    "Area_mm2":[area]
})
df["Stress_Nmm2"]=df["Axial_kN"]*1000 / df["Area_mm2"]
if st.button("Submit"):
 st.dataframe(df)
"""

#                            EXAMPLE 2 
# GOAL : CREATE A STATUS COLUMN AFTER CHECKING ALLOWABLE OR NOT 
"""
import streamlit as st
import pandas as pd
data={
    "Column":["C1","C2","C3","C4"],
    "Axial_kN":[450,600,380,0.00000003],
    "Area_mm2":[2500,3000,2200,1.0]
}
allowable=0.4    # EXAMPLE 0.4 Nmm2
df=pd.DataFrame(data)
df["Stress_Nmm2"]=df["Axial_kN"]*1000 / df["Area_mm2"]
df["Status"] = df["Stress_Nmm2"] >= allowable
if st.button("Submit") : 
    st.dataframe(df)   
"""

# CONCEPT 6 : EDITABLE / INTERACTIVE TABLES IN STREAMLIT 

#                                  EXAMPLE 1
"""
import streamlit as st 
import pandas as pd
st.title("Editable Table")
df=st.data_editor(
    pd.DataFrame(
        {
            "Columns":["C1","C2","C3","C4","C5","C6"],
            "Name":["Shivam","Anjali","Pushpa","Papa","Mummy","Pussy Cat"],
            "role":["Engineer","Nurse","Student","Guardian","Guardian","Student"]
        }
    ),num_rows="dynamic"
)
if st.button("Submit"):
    df["Status"]=df["Name"]+" Is "+df["role"]
    st.dataframe(df)
"""