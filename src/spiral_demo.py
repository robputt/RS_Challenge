'''
Created on 12 Nov 2014

@author: robert_putt
'''

from spiral_array import spiral_array, print_2d_array, array_generator

#Generate a sample array to use against the spiral function.
input_array = array_generator(4,4)

#Print the array so it is easier for debug.
print "Input Array:"
print_2d_array(input_array)

#Print the output.
print ""
print "Output Array:"
print spiral_array(input_array)
