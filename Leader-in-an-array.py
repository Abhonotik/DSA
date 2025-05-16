import numpy as np
arr = np.array([2, 1, 3, 4, 5, 3])

last = arr[-1]
leader = [int(last)]  

for i in arr[-2::-1]:  
    if i > last:
        leader.append(int(i))
        last = i

leader.reverse()
print("Leaders:", leader)
