''' Test numpy with ctypes.  Test to compare performance of NumPy vs NumRs '''

import ctypes
from time import time

# Load NumRs library as rs
rs = ctypes.cdll.LoadLibrary('code/NumRS/src/libNumRs.dll')


# # Test 1: sum of 1 million random numbers
# def test1():
#     ''' Test sum of 1 million random numbers '''
#     start = time()
#     print("Test 1: sum of 1 million random numbers")
#     # Generate random numbers from 0 to 99 inclusive (100000 numbers)
#     nums = [rnd.randint(0, 99) for i in range(1000000)]
#     # Sum with NumPy
#     np_sum = np.sum(nums)
#     print("NumPy sum: ", np_sum)
#     print("NumPy time: ", time() - start)


# # Test 2: sum of 1 million random numbers with NumRs
# def test2():
#     ''' Test sum of 1 million random numbers '''
#     start = time()
#     print("Test 1: sum of 1 million random numbers")
#     # Generate random numbers
#     nums = [rnd.random() for i in range(1000000)]
#     # Sum with NumRs
#     rs_sum = rs.sum(nums, len(nums))
#     print("NumRs sum: ", rs_sum)
#     print("NumRs time: ", time() - start)

# Test 1: pythons hello world
def test1():
    ''' Test pythons hello world '''
    start = time()
    print("Hello world")
    print("Time: ", time() - start)


def test2():
    ''' Test pythons hello world '''
    start = time()
    rs.hello_world()
    print("Time: ", time() - start)


def execute():
    ''' Execute tests '''
    test1()
    test2()


# Execute tests
if __name__ == '__main__':
    execute()
