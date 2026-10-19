import numpy as np

def check ():
    no = 0
    c= set()
    while len(c)!=6:
        x= rng.integers(1, 7)
        c.add(x)
        no+=1
    return no
rng =np.random.default_rng(10)
arr = np.array([check() for seed in range(20000)])
print (np.mean(arr))
print (np.percentile(arr, 90))
