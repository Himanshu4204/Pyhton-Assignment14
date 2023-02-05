# Q9. Write a Python script to print indices of all occurrences of a given element in a given list.?
l=[1,5,3,1,5,4]
indices=[i for i in range(len(l)) if l[i]==1]
print(indices)