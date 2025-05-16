#An array (or list) of numbers → e.g., [3, 1, 2, 2, 1, 2, 3, 3]
#An integer k → e.g., k = 4
#Your task is to find all elements in the array that appear more than n/k times, where:
#n = length of the array
#n/k = the threshold for how many times an element must appear to be included in the answer


arr=[3, 1, 2, 2, 1, 2, 3, 3]
n=len(arr)
k=4

frequence={}
for i in arr:
    if i in frequence:
        frequence[i]+=1
    else:
        frequence[i]=1

for j in frequence:
    if frequence[j]>2:
        print(j)

        


    
    
    
    
    
    

