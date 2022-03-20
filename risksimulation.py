#Silas Clymer 4/26/21
#Approximates p(X)
#where X is number of armies lost by attacker in a round of Risk

import random

def clash():
    loss = 0
    A = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    D = [random.randint(1,6), random.randint(1,6)]
    if max(A) <= max(D):
        loss += 1
    A.remove(max(A))
    D.remove(max(D))
    if max(A) <= max(D):
        loss += 1
    return loss
    

def simulate(n):
    zeros = 0
    ones = 0
    twos = 0
    for i in range(n):
        X = clash()
        if X == 0:
            zeros += 1
        elif X == 1:
            ones += 1
        else:
            twos += 1
    return zeros/n, ones/n, twos/n

print(simulate(1000000))

#With a million simulations, my most recent result was:
#p(0) = .371348
#p(1) = .336431
#p(2) = .292221


    

    
