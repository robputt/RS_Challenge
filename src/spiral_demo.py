'''
Created on 12 Nov 2014

@author: robert_putt
'''

from spiral_array import spiral_array, print_2d_array, array_generator

#Define a 2D array to test the spiral_array function. In this case 3x3.
input_array = array_generator(3,8)

#Print the array so it is easier for debug.
print "Input Array:"
print_2d_array(input_array)

#Print the output.
print ""
print "Output Array:"
print spiral_array(input_array)
