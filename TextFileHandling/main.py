#Exercise-1
"""
with open("notes.txt","w") as f:
    f.write("I am learning file handling.\nI want to automate civil engineering tasks.\nPython will help me do that.")
   
with open("notes.txt","r") as f:
    for line,data in enumerate(f,start=1):
        print(f"Line {line} : {data.strip()}") 
"""

#Exercise_2 
"""
with open("lab_record.txt","w") as f:
    f.write("Soil Test Record:\nMoisture Content Data:")

with open("lab_record.txt","a") as f:
    f.write("Sample 1 = 14.5%\nSample 2 = 19.2%\nSample 3 = 11.8%")
"""

#Exercise-3
"""
with open("moisture_data.txt","w") as f:
    f.write("SampleName,Moisture,UnitWeight\nS1,14.5,18.2\nS2,19.2,17.6\nS3,11.8,19.0")

with open("moisture_data.txt","r") as f:
    for index,data in enumerate(f):
        data=data.strip()
        data=data.split(",")
        print(f"Sample {data[0]} -> Moisture : {data[1]}%, UnitWeight : {data[2]}KN/m3")
"""

#Exercise-4
"""
with open("field_density.txt","w") as f:
    f.write("TestID,WetDensity,DryDensity\nT1,18.5,16.2\nT2,19.1,17.0\nT3,17.8,15.5")

with open("field_density.txt","r") as f:
    for index,data in enumerate(f):
        if index!=0:
            data=data.strip()
            data=data.split(",")
            dos=(float(data[2])/float(data[1]))*100
            print(f"{data[0]} -> Degree Of Saturation : {dos:.3f}% ")
"""

#Exercise-5
"""
with open("soil_properties.txt","w") as f:
    f.write("SoilType=Clay\nPlasticLimit=22.5\nLiquidLimit=39.2\nSpecificGravity=2.68\nOptimumMoisture=16.4")

with open("soil_properties.txt","r") as f:
    data_dic={}
    for data in f:
        data=data.strip().split("=")
        try:
            data[1]=float(data[1])
        except:
            pass
        key,value=data[0],data[1]  
        data_dic[key]=value
    print(data_dic) 
"""             

#Exercise_6
"""
with open("survey_coords.txt","w") as f:
    f.write("East North Elevation\n100.5 200.7 150.2\n101.2 201.3 149.8\n102.0 202.0 150.1\n99.8 199.9 150.5")

with open("survey_coords.txt","r") as f:
    data_l=[]
    for index,data in enumerate(f):
        if index!=0:
            data=data.strip().split(" ")
            for index2,data2 in enumerate(data,start=0):
                try:
                    data[index2]=float(data[index2])
                except:
                    pass
            data_l.append(tuple(data))   
print(data_l)  
"""

#Exercise-7
"""
with open("sensor_log.txt","w") as f:
    f.write("Time Load(kN) Settlement(mm)\n1  120    2.5\n2  ERR    2.8\n3  135    N\n4  200    3.1\n5  -50    2.0\n6  145    2.9\n7  9999   2.6")

with open("sensor_log.txt","r") as f:
    cleaned=[]
    for index,data in enumerate(f):
        data=data.strip().split()
        if index!=0:
            for index2,data2 in enumerate(data):
                try:
                    data[index2]=float(data[index2])
                except:
                    data[index2]=None
            if any(v is None for v in data ):
                continue
            if (data[1]>1000 or data[1]<0):
                continue
            if  (data[2]>1000 or data[2]<0):
                continue      
            cleaned.append(tuple(data))
print(cleaned)   
"""        







































