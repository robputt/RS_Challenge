'''
Created on 12 Nov 2014

@author: robert_putt
'''

def spiral_array(input_array):
    '''
        Takes an array and unravels it into an array of values in a
        spiral fashion in a clockwise direction from [0,0]

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
    total_values = dimensions['x'] * dimensions['y']
    output_array = []
    not_done = True

    while not_done:
        #Get the top row...
        while current_x < (dimensions['x'] - layer):
            output_array.append(input_array[current_y][current_x])
            current_x += 1

        current_x -= 1
        current_y += 1

        #Get the right side...
        while current_y < (dimensions['y'] - layer):
            output_array.append(input_array[current_y][current_x])
            current_y += 1

        current_y -= 1
        current_x -= 1

        #Get the bottom...
        while current_x > (-1 + layer):
            output_array.append(input_array[current_y][current_x])
            current_x -= 1

        current_x += 1
        current_y -= 1

        #Get the left side...
        while current_y > (0 + layer):
            output_array.append(input_array[current_y][current_x])
            current_y -= 1

        current_x += 1
        current_y += 1

        #If not done move on to the next layer in and repeat.
        if len(output_array) >= total_values:
            not_done = False
            output_array = output_array[0:total_values]
        else:
            layer += 1

    return output_array

def print_2d_array(input_array):
    '''
        Takes a 2D array and prints it to stdout.

        Args:
                    input_array - A 2 dimensional array of any size.

    '''
    dimensions = get_array_dimensions(input_array)
    print "Dimensions %sx%s" % (dimensions['x'], dimensions['y'])

    for row in range(0, dimensions['y']):
        row_output = ""
        for column in range(0, dimensions['x']):
            row_output = "%s %s" % (row_output, input_array[row][column])
        print row_output

def get_array_dimensions(input_array):
    '''
        Takes a 2D array and returns it's dimensions in the form of a dictionary

        Args:
                    input_array - A 2 dimensional array of any size.

        Returns:
                    dictionary - In the form:
                                 {'x': <x_length>, 'y': <y_length>}
    '''
    return {"y":len(input_array), "x":len(input_array[(len(input_array) - 1)])}

def array_generator(x_length, y_length):
    '''
        Takes required x and y length of array and generated a 2D array
        with specified lengths and generated dummy numerical data.

        Args:
                    x_lenght - length of x side of array (int)
                    y_length - length of y side of array (int)

        Returns:
                    array - 2D array of specified size with dummy data.
    '''
    output_array = [[0 for lx in xrange(x_length)] for ly in xrange(y_length)]
    counter = 1

    for row in range(0, y_length):
        for column in range(0, x_length):
            output_array[row][column] = counter
            counter += 1

    return output_array
