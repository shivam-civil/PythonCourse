
#Exercise of __init__(self)
"""
class Beam:
    def __init__(self,length):
        self.length=length
"""        


#Exercise of __str__(self)
"""
class Beam:
    def __init__(self,length):
        self.length=length
    def __str__(self):
        return f"Beam Length : {self.length}"
obj=Beam(10)
print(obj)  # for __str__(self)
"""      

#Exercise of __repr__(self)
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


#Exercise of __len__()
"""
class SiteTasks:
    def __init__(self,tasks):
        self.tasks=tasks
    def __len__(self):
        return len(self.tasks) 
obj=SiteTasks(["BeamCast","ColumnCast","Excavation","Curing"])
print(len(obj))     
"""   

#Exercise of 