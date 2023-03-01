''' Test numpy with ctypes.  Test to compare performance of NumPy vs NumRs '''

from ctypes import cdll
from time import time
import random as rnd
import numpy as np

# Load NumRs library as rs
rs = cdll.LoadLibrary("NumRs.dll")


# Test 1: sum of 1 million random numbers
def test1():
    ''' Test sum of 1 million random numbers '''
    start = time()
    print("Test 1: sum of 1 million random numbers")
    # Generate random numbers from 0 to 99 inclusive (100000 numbers)
    nums = [rnd.randint(0, 99) for i in range(1000000)]
    # Sum with NumPy
    np_sum = np.sum(nums)
    print("NumPy sum: ", np_sum)
    print("NumPy time: ", time() - start)


# Test 2: sum of 1 million random numbers with NumRs
def test2():
    ''' Test sum of 1 million random numbers '''
    start = time()
    print("Test 1: sum of 1 million random numbers")
    # Generate random numbers
    nums = [rnd.random() for i in range(1000000)]
    # Sum with NumRs
    rs_sum = rs.sum(nums, len(nums))
    print("NumRs sum: ", rs_sum)
    print("NumRs time: ", time() - start)


# Execute tests
test1()
test2()
