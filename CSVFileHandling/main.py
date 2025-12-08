#CSVFileHandling
from csv import reader,DictReader,writer,DictWriter
#Example-1: Reading a csv file and printing its content with reader().

"""
with open("data.csv","r") as f:
    reader=reader(f)
    print(list(reader))

    for row in reader:
        print(row)

    Note : reader() stores the row wise data normally as list form but also includes the header part.    
"""        
   

#Example-2: Reading a csv file and printing its content with DictReader()
"""
with open("data.csv","r") as f:
    reader=DictReader(f)
    for row in reader:
        print(row)
        print(row["Name"],row["Physics"])

 #  Note : DictReader() stores every row data as dictionary with key as header.     
"""
#Example-3: Writing rows data to data.csv file using writerow()
"""
with open("data.csv","a",newline="") as f:
    writer=writer(f)
    writer.writerow(["Shivam","99","99","98"])
"""

#Example-4: Writing rows data to data.csv file using DictWriter()
"""
with open("data.csv","a",newline="") as f:
    headers=["Name","Maths","Physics","Computer"]
    writer=DictWriter(f,fieldnames=headers)
    writer.writeheader()
    writer.writerow({"Name":"Shyam","Maths":"99","Physics":"99","Computer":"100"})
"""

#Exercise-1 : Write Python code to read all rows and print them one by one using csv.reader() from file materials.csv
"""
with open("materials.csv","r") as f:
    reader=reader(f)
    for row in reader:
        print(row)
"""
#Exercise-2: Print only the Material column using csv.reader() (NOT DictReader yet).File : materials.csv
"""
with open("materials.csv","r") as f:
    r=reader(f)
    for row in r:
        print(row[0])
"""

#Exercise-3: Print the output in this format:(File: materials.csv) using DictReader()
#     Cement → 10 bags
#     Sand → 5 bags
#     Aggregates → 15 bags
"""
with open("materials.csv","r") as f:
    r=DictReader(f)
    for row in r:
        print(f" {row['Material']} -> {row['Quantity']}")
"""

#Exercise-4: WRITE TO A CSV (using csv.writer). File : new_materials.csv
#Material,Quantity,UnitRate
#Bricks,5000,12
#Steel,200,110
#Cement,20,550
"""
with open("new_materials.csv","w",newline="") as f:
    w=writer(f)
    w.writerow(["Material","Quantity","UnitRate"])
    w.writerow(["Bricks","5000","12"])
    w.writerow(["Steel","200","110"])
    w.writerow(["Cement","20","550"])
"""

#Exercise-5: Add a new material row to existing CSV (new_materials.csv) without overwriting old data. Glass,50,80
"""
#Using DictWriter()

with open("new_materials.csv","a",newline="") as f:
    headers=["Material","Quantity","UnitRate"]
    w=DictWriter(f,fieldnames=headers)
    w.writerow({"Material":"Glass","Quantity":"50","UnitRate":"80"})

#Using writer()

with open("new_materials.csv","a",newline="") as f:
    w=writer(f) 
    w.writerow(["Glass","50","80"])
"""
#Exercise-6: Update the Quantity of Steel in new_materials.csv from 200 → 250.
"""
with open("new_materials.csv","r") as f:
    r=DictReader(f)
    new_data=[]
    for row in r:
        if row["Material"]=="Steel":
            row["Quantity"]=250
        new_data.append(row)    

    with  open("new_materials.csv","w",newline="") as f:
     w=DictWriter(f,fieldnames=r.fieldnames) 
     w.writeheader()
     w.writerows(new_data)
"""

#Exercise-7: Read new_materials.csv and print only materials with Quantity > 50.
"""
with open("new_materials.csv","r") as f:
    r=DictReader(f)
    for row in r:
        if float(row["Quantity"])>=float(50):
            print(f"{row['Material']} : {row['Quantity']}pieces {row['UnitRate']}UnitRate")
"""

#Exercise-8: Calculate total cost per material and save it to a new CSV (materials_cost.csv)
"""
with open("materials.csv","r") as f:
    updated=[]
    r=DictReader(f)
    for data in r:
        total_cost=float(data.get("Quantity"))*float(data.get("UnitRate"))
        data["TotalCost"]=str(total_cost)
        updated.append(data)
with open("materials_cost.csv","w",newline="") as f:
    headers=["Material","Quantity","UnitRate","TotalCost"]
    w=DictWriter(f,fieldnames=headers)
    w.writeheader()
    w.writerows(updated)   
"""

#Exercise-9: Filter materials with TotalCost > 5000 and save them into a new CSV (costly_materials.csv)
"""
with open("materials_cost.csv","r") as f:
    updated=[]
    r=DictReader(f)
    for data in r:
        if float(data.get("TotalCost"))>5000:
            updated.append(data)
with open("costly_materials.csv","w",newline="") as fw:
    w=DictWriter(fw,fieldnames=r.fieldnames)
    w.writeheader()
    w.writerows(updated) 
"""

#Exercise-10:Sort by TotalCost descending and save. Read from materials_cost.csv and write to materials_sorted.csv
"""
#First Step: Read the datas from file materials_cost.csv
with open("materials_cost.csv","r") as f:
    r=DictReader(f)
    data=list(r)
#second Step: Sort it by TotalCost(descending order)
data_sorted=sorted(data,reverse=False,key= lambda x:float(x.get("TotalCost")))
#Third Step: Write it to materials_sorted.csv
with open("materials_sorted.csv","w",newline="") as fw:
    w=DictWriter(fw,fieldnames=r.fieldnames)
    w.writeheader()
    w.writerows(data_sorted)
"""
    







          







   
 
