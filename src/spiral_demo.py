'''
Created on 12 Nov 2014

@author: robert_putt
'''

from spiral_array.__init__ import spiral_array, print_2d_array

#Define a 2D array to test the spiral_array function. In this case 3x3.
input_array = [[0 for x in xrange(10)] for x in xrange(6)]

#Populate with some sample data which is easy to unravel for testing.
input_array[0][0] = 1
input_array[0][1] = 2
input_array[0][2] = 3
input_array[0][3] = 4
input_array[0][4] = 5
input_array[0][5] = 6
input_array[0][6] = 7
input_array[0][7] = 8
input_array[0][8] = 9
input_array[0][9] = 10
input_array[1][0] = 11
input_array[1][1] = 12
input_array[1][2] = 13
input_array[1][3] = 14
input_array[1][4] = 15
input_array[1][5] = 16
input_array[1][6] = 17
input_array[1][7] = 18
input_array[1][8] = 19
input_array[1][9] = 20
input_array[2][0] = 21
input_array[2][1] = 22
input_array[2][2] = 23
input_array[2][3] = 24
input_array[2][4] = 25
input_array[2][5] = 26
input_array[2][6] = 27
input_array[2][7] = 28
input_array[2][8] = 29
input_array[2][9] = 30
input_array[3][0] = 31
input_array[3][1] = 32
input_array[3][2] = 33
input_array[3][3] = 34
input_array[3][4] = 35
input_array[3][5] = 37
input_array[3][6] = 37
input_array[3][7] = 38
input_array[3][8] = 39
input_array[3][9] = 40
input_array[4][0] = 41
input_array[4][1] = 42
input_array[4][2] = 43
input_array[4][3] = 44
input_array[4][4] = 45
input_array[4][5] = 46
input_array[4][6] = 47
input_array[4][7] = 48
input_array[4][8] = 49
input_array[4][9] = 50
input_array[5][0] = 51
input_array[5][1] = 52
input_array[5][2] = 53
input_array[5][3] = 54
input_array[5][4] = 55
input_array[5][5] = 56
input_array[5][6] = 57
input_array[5][7] = 58
input_array[5][8] = 59
input_array[5][9] = 60



#Print the array so it is easier for debug.
print "Input Array:"
print_2d_array(input_array)

#Print the output.
print ""
print "Output Array:"
print spiral_array(input_array)
