import numpy as np

# File: mystats.py
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

# define the mean function here
def mean(*numbers):
    add=0
    length=0
    try:
        for i in numbers:
            if is_iter(i):
                add+=sum(i)
                length+=len(i)
            else:
                add+=i
                length+=1
        means=add/length
        return means
    except:
        means='FAIL'
    return means

# define the stddev function here
def stddev(*numbers):
    means=mean(*numbers)
    add=0
    length=0
    for i in numbers:
        if is_iter(i):
            for j in i:
                add+=(j-means)**2
                length+=1
        else:
            add+=(i-means)**2
            length+=1
    std=(add/(length-1))**0.5
    return std

# define the median function here
def median(*numbers):
    sorts=[]
    for i in numbers:
        if is_iter(i):
            for j in i:
                sorts.append(j)
        else:
            sorts.append(i)
    sorts=np.sort(sorts)
    length=len(sorts)
    if length%2==0:
        med=(sorts[int(length/2-1)]+sorts[int(length/2)])/2
    else:
        med=sorts[int((length-1)/2)]
    return med
            
# define the mode function here
def mode(*numbers):
    num={}
    modes=[]
    for i in numbers:
        if is_iter(i):
            for j in i:
                if j in num:
                    num[j]=num[j]+1
                else:
                    num[j]=1
        else:
            if i in num:
                num[i]=num[i]+1
            else:
                num[i]=1
    for key,value in num.items():
        if (value==max(num.values())):
            modes.append(key)
    if len(modes)>1:        
        modes=tuple(modes)  
    else:
        modes=modes[0]
    return modes

if __name__=='__main__':
    
    # part (a)
    print('The current module is:', __name__)#The current module is: __main__
    
    # part (b)
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:',mean(1,2,3,4))
    print('mean(2.4,3.1) should be 2.75, and is:',mean(2.4,3.1))
    print('mean() should FAIL:', mean())
    
    # part (c)
    print('mean([1,1,1,2]) should be 1.25, and is:',mean([1,1,1,2]))
    print('mean((1,), 2, 3, [4,6]) should be 3.2,' +'and is:', mean((1,), 2, 3, [4,6]))
    
    # part (d)
    # your code here
    for i in range(10):
        print("Draw", i, "from Norm(0,1):",np.random.randn())
        
    ls50 = [np.random.randn() for i in range(50)]
    print("Mean of", len(ls50), "values from Norm(0,1):",mean(ls50))
    
    ls10000 = [np.random.randn() for i in range(10000)]
    print("Mean of", len(ls10000), "values from "+"Norm(0,1):", mean(ls10000))
    # part (e)
    # your code here
    np.random.seed(0)
    a1 = np.random.randn(10)
    print("a1:", a1)
    print("the mean of a1 is:", mean(a1))
    # part (f)
    # your code here
    print("the stddev of a1 is:", stddev(a1))
    # part (g)
    # your code here
    print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))
    # part (h)
    # your code here
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:",mode(1, 2, (1, 3), 3, [1, 3, 4]))