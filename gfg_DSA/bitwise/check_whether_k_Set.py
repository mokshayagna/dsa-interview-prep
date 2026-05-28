a = 23
k = 2

"""
         5 4 3 2 1 0    
    23 = 0 1 0 1 1 1
   o/p & 0 0 0 1 0 0 True for k= 2
   
         5 4 3 2 1 0    
    23 = 0 1 0 1 1 1  False for k = 3
       & 0 0 1 0 0 0  
       
"""

b = a & (1<<k)

if b == 0:
    print(False)
else:
    print(True)
