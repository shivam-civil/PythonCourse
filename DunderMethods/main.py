
#Exercise of __init__(self)
"""
class Beam:
    def __init__(self,length):
        self.length=length
"""        


#Exercise of __str__(self)   for Human Reading
"""
class Beam:
    def __init__(self,length):
        self.length=length
    def __str__(self):
        return f"Beam Length : {self.length}"
obj=Beam(10)
print(obj)  # for __str__(self)
"""      

#Exercise of __repr__(self)    For Developer's Reading
"""
class Beam:
    def __init__(self,length):
        self.length=length
    def __str__(self):
        return f"Beam Length : {self.length}"
    def __repr__(self):
        return f"Beam(length='{self.length}')"
obj=Beam(10)
print([obj])   #for __repr__
"""


#Exercise of __len__(self)
"""
class SiteTasks:
    def __init__(self,tasks):
        self.tasks=tasks
    def __len__(self):
        return len(self.tasks) 
obj=SiteTasks(["BeamCast","ColumnCast","Excavation","Curing"])
print(len(obj))     
"""   

#Exercise of __getitem__(self)
"""
class Beam:
    def __init__(self,details):
        self.details=details
    def __getitem__(self,index):
        return self.details[index]
obj=Beam(["beam1","20*20",45])
print(obj[0]) 
"""       

#Exercise of __setitem__(self)
"""
class Beam:
    def __init__(self,details):
        self.details=details
    def __getitem__(self,index):
        return self.details[index]
    def __setitem__(self,key,value):
        self.details[key]=value
    def __str__(self):
        return str(self.details) 
    def __len__(self):
        return len(self.details)       

obj=Beam(["beam1","20*20",45])
obj[0]="Beam2"
print(obj)
"""





