# Q3. Write a python script to create a list of first N Even Natural Numbers ?
x=int(input("Enter a Number :"))
l1=[]
for a in range(2,2*x+1):
    if a%2==0:
        l1.append(a)
print(l1)