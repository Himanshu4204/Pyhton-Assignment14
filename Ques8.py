# Q8.Write a Python script to print distinct elements along with their frequencies of occurrence in the list?
l1=[1,1,2,3,3,2,21,1,3,1]
freq={}
for i in l1:
    if(i in freq):
        freq[i]+=1
    else:
        freq[i]=1

for key, value in freq.items():
    print("%d : %d"%(key,value))
