import numpy as np

class Bound:
    def __init__(self, high_or_low, inclusive, value):
        self.__validate_arguments(high_or_low)
        self.high_or_low = high_or_low
        self.inclusive = inclusive
        self.value = value

    def __validate_arguments(self, high_or_low):
        if high_or_low != 'high' and high_or_low != 'low':
            raise ValueError("high_or_low flag must be 'high' or 'low'")
        
    def bound_to_operator(self):
        if self.high_or_low == 'high' and self.inclusive == True:
            return '<='
        elif self.high_or_low == 'high' and self.inclusive == False:
            return '<'
        elif self.high_or_low == 'low' and self.inclusive == True:
            return '>='
        elif self.high_or_low == 'low' and self.inclusive == False:
            return '>'

class Inequality:
    def __init__(self, operation, value):
        self.__validate_arguments(operation)
        self.bounds = []

        self.add_bound(operation, value)

        self.high_bound = Bound('high', True, np.inf)
        self.low_bound = Bound('low', True, -1*np.inf)
        self.valid = True

    def __validate_arguments(self, operation):
        if operation != '<' and operation != '<=' and operation != '>' and operation != '>=':
            raise ValueError("Operation must be '<', '<=', '>' or '>='")
        
    def add_bound(self, operation, value):
        if operation == '<':
            self.bounds.append(Bound('high', False, value))
        elif operation == '<=':
            self.bounds.append(Bound('high', True, value))
        elif operation == '>':
            self.bounds.append(Bound('low', False, value))
        elif operation == '>=':
            self.bounds.append(Bound('low', True, value))

    def combine_bounds(self):
        self.high_bound = Bound('high', True, np.inf)
        self.low_bound = Bound('low', True, -1*np.inf)
        for inequality_bound in self.bounds:
            if inequality_bound.high_or_low == 'high':
                if inequality_bound.value < self.high_bound.value:
                    self.high_bound.value = inequality_bound.value
                    self.high_bound.inclusive = inequality_bound.inclusive
                elif inequality_bound.value == self.high_bound.value:
                    if inequality_bound.inclusive == False:
                        self.high_bound.inclusive = False
            else:
                if inequality_bound.value > self.low_bound.value:
                    self.low_bound.value = inequality_bound.value
                    self.low_bound.inclusive = inequality_bound.inclusive
                elif inequality_bound.value == self.low_bound.value:
                    if inequality_bound.inclusive == False:
                        self.low_bound.inclusive = False

        if self.high_bound.value < self.low_bound.value:
            self.valid = False

    def print_bounds(self):
        if self.valid:
            print(f"{self.low_bound.value} {self.low_bound.bound_to_operator()} x {self.high_bound.bound_to_operator()} {self.high_bound.value}")
        else:
            print("No valid values for this inequality")

if __name__=='__main__':
    # Test of class behaviour
    test_inequality = Inequality('>', 5)
    test_inequality.add_bound('<=', 8)
    test_inequality.add_bound('<', 7)
    test_inequality.add_bound('<=', 7)

    test_inequality.combine_bounds()
    test_inequality.print_bounds()
