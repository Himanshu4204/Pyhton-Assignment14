# Q7. write a python script to remove all non int values from a list ?
l1=[12,True,4.5,4+5j,"Himanshu",45,"MySirG"]
l1=[x for x in l1 if type(x)==int]
print(l1)

