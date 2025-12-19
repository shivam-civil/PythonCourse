class Beam:
 def __init__(self,items):
  self.items=items
 def __len__(self):
  return len(self.items)
 def __str__(self):
  return f"Items : {self.items})"
 def __repr__(self):
  return f"Beam(items={self.items})"
 def __getitem__(self,index):
  return self.items[index]
 def __setitem__(self,index,value):
  self.item[index]="Excavation"

obj=Beam(["Survey","Design","Excavation","Construction"])
print(obj) # str call
print([obj])  #repr call
print(len(obj)) #len call
print(obj[0])  #getitem  call
               #setitem call