# Q2. Write a python script to create a list of first N Odd Natural Numbers ?
x=int(input("Enter a Number :"))
l1=[]
for a in range(1,2*x+1):
    if a%2!=0:
        l1.append(a)
print(l1)