'''
Created on 12 Nov 2014

@author: robert_putt
'''

from spiral_array.__init__ import spiral_array, print_2d_array

#Define a 2D array to test the spiral_array function. In this case 3x3.
input_array = [[0 for x in xrange(3)] for x in xrange(3)]

#Populate with some sample data which is easy to unravel for testing.
input_array[0][0] = 1
input_array[0][1] = 2
input_array[0][2] = 3
input_array[1][0] = 4
input_array[1][1] = 5
input_array[1][2] = 6
input_array[2][0] = 7
input_array[2][1] = 8
input_array[2][2] = 9

#Print the array so it is easier for debug.
print "Input Array:"
print_2d_array(input_array)

#Print the output.
print ""
print "Output Array:"
print spiral_array(input_array)
