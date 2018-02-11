'''
Finding the first 100 unrestricted partitions.
Patrick McMillin
PHYS 431, Dr. Taheri
Last modified: 4 December 2017
'''

def Generate_Unrestricted_Partitions():
    # Finding pentagonal numbers to be used in Euler's formula
    Pentagonal_Numbers = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])
    # Initial unrestricted partition (requires initial condition). Unrestricted partition of 0 is 1.
    n = 0
    Unrestricted_Partitions = [1]
    # Sign convention for expanding Euler's formula
    Sign_Convention = [1, 1, -1, -1]
    # Looping over all numbers, finding unrestricted partitions for the first 100 numbers.
    while n < 100:
        n += 1 #iterate
        Unrestricted_Partition_for_n = 0 # To be added to in Euler's formula.
        i = 0 # Iterable for pentagonal numbers summed over in Euler's formula.
        while Pentagonal_Numbers[i] <= n: # Defined only for n-p >=0
            # Adds to the unrestricted partition by Euler's formula. Ensures proper sign convention.
            Unrestricted_Partition_for_n += Unrestricted_Partitions[n - Pentagonal_Numbers[i]] * Sign_Convention[i % 4]
            i += 1 # iterate
            # Add our newly found unrestricted partition to the list.
        Unrestricted_Partitions.append(Unrestricted_Partition_for_n)            
    return Unrestricted_Partitions
Unrestricted_Partitions = Generate_Unrestricted_Partitions()
Integer_List = range(0,100)
import numpy as np
np.savetxt('Unrestricted_Partitions.csv', Unrestricted_Partitions, fmt='%10.5f', delimiter=',')
