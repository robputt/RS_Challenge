'''
Created on 12 Nov 2014

@author: robert_putt
'''

def spiral_array(input_array):
    '''
        Takes an array and direction and unravels it into an array of
        values in a spiral fashion in a clockwise direction from [0,0]

        Args:
                    input_array - A 2 dimensional array of any size

        Returns:
                    array - Array of values from the input_array
                            in clockwise spiral order.
    '''
    dimensions = get_array_dimensions(input_array)
    current_x = 0
    current_y = 0
    layer = 0
    output_array = []

    

    return output_array

def print_2d_array(input_array):
    dimensions = get_array_dimensions(input_array)
    print "Dimensions %sx%s" % (dimensions['y'], dimensions['x'])

    for row in range(0, dimensions['y']):
        row_output = ""
        for column in range(0, dimensions['x']):
            row_output = "%s %s" % (row_output, input_array[row][column])
        print row_output

def get_array_dimensions(input_array):
    return {"y":len(input_array), "x":len(input_array[(len(input_array) - 1)])}
