#Silas Clymer 4/26/21
#Approximates p(A <= 3)
#where A is number of armies lost by attacker in a 4 rounds of risk

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
    t = 0
    for i in range(n):
        A = clash() + clash() + clash() + clash()
        if A <= 3:
            t += 1
    return t/n
        
print(simulate(1000000))

#P(A <= 3) is approximately 0.461301


    

    
