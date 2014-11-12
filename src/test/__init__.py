import unittest
from spiral_array import array_generator, get_array_dimensions, spiral_array

class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_spiral_array(self):
        in_array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
        result = spiral_array(in_array)
        expected_array = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
        self.assert_(result == expected_array, "Unexpected result returned from spiral_array function")
        in_array = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[11,12,13,14,15],\
                    [6,7,8,9,10],[1,2,3,4,5]]
        result = spiral_array(in_array)
        expected_array = [1, 2, 3, 4, 5, 10, 15, 20, 15, 10, 5, 4, 3, 2, 1, 6, 11, 16, 11, 6, 7, 8, 9,\
                          14, 19, 14, 9, 8, 7, 12, 17, 12, 13, 18, 13]
        self.assert_(result == expected_array, "Unexpected result returned from spiral_array function")

    def test_get_array_dimensions(self):
        result = get_array_dimensions([[0,1,2],[3,4,5],[6,7,8]])
        self.assert_(result == {'x':3,'y':3}, "Incorrect value returned from get_array_dimensions function")
        result = get_array_dimensions([[0],[3],[6]])
        self.assert_(result == {'x':1,'y':3}, "Incorrect value returned from get_array_dimensions function")
        result = get_array_dimensions([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],\
                                       [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
        self.assert_(result == {'x':7,'y':6}, "Incorrect value returned from get_array_dimensions function")

    def test_array_generator(self):
        result = array_generator(2, 2)
        self.assert_(result == [[1,2],[3,4]], "Unexpected result returned from array_generator function")
        result = array_generator(10, 6)
        self.assert_(result == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], \
                                [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], \
                                [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]], \
                     "Unexpected result returned from array_generator function")
        result = array_generator(4, 8)
        self.assert_(result == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20],\
                                [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]], \
                     "Unexpected result returned from array_generator function")
