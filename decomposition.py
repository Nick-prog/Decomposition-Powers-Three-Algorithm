import numpy as np

class Decomposition():
    '''
    Class created to house all logic required for the project.
    '''

    def __init__(self, input):
        self.input = input

    def get_highest_power(self):
        '''
        Helper method designed to find the highest possible power to start off with based on lower-end of each range.
        1: {1}
        3: {2, 4}
        9: {5, 13}
        27: {14, 40}
        81: {41, 121}
        Return count (power)
        '''
        abs_input = abs(self.input)
        range_caps = [1, 2, 5, 14, 41]
        count = -1
        for x in range_caps:
            if(abs_input >= x):
                count += 1
        return count


    def decomposition_powers_three(self):
        '''
        Decomposes the inputted value into an expression of only powers of 3.
        power = highest possible power between 1, 3, 9, 27, and 8.
        value = starting point for our arthimetic operations. Ex: 27-3+1.
        Return a list of arthimetic operations used to generate input.
        '''
        power = self.get_highest_power() # Acquire the starting power.
        
        value = 3**power # Calculate the starting value based on power.
        power -= 1 # Decrement since the value has already been used and recorded.

        if(self.input < 0): # Starting value for negative inputs.
            value = -value

        order_list = [value] # List to store all operations. Holds the first value at the start.

        result = self.input - value # Keeps track of the current progression, helps find special cases.

        while(value != self.input):
            if(abs(result) == 1): # If a special case, next operation starts off at 3^0.
                power = 0
                result = 0
            elif(2 <= abs(result) <= 4): # If a special case, next operation starts off at 3^1.
                power = 1
                result = 0
            elif(5 <= abs(result) <= 13): # If a special case, next operation starts off at 3^2.
                power = 2
                result = 0
            else: # Iterate through the allowed multiples of 3. Ex: 3^3, 3^2, etc...
                if(value > self.input): # Value is too high, need to subtract.
                    value = value - 3**power
                    append_str = f'- {3**power}'
                    order_list.append(append_str)
                    power -= 1 # Decrement to next allowed multiple of 3.
                    result = self.input - value # Check for special case.
                else: # Value is too low, need to add.
                    value = value + 3**power
                    append_str = f'+ {3**power}'
                    order_list.append(append_str)
                    power -= 1 # Decrement to next allowed multiple of 3.
                    result = self.input - value # Check for special case.
                
        return order_list

if __name__ == '__main__':
    input = 121
    decomp = Decomposition(input)
    order_list = decomp.decomposition_powers_three()
    print(order_list)