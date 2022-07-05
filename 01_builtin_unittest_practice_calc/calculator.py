'''calculator class for studying built-in unittest module
    Written by: Giseop Noh
'''

class Calculator:
    '''Calculator class'''

    def __init__(self) -> None:
        self.version = '1.0.0'
        self.manufacturer = 'CJU university'

    @property
    def info(self,) -> None:
        '''Display calculator information'''
        print(f'\nCalculator version: {self.version}')
        print(f'Made by {self. manufacturer}\n')


    def add(self, num1, num2):
        """Add Function"""
        return num1 + num2


    def subtract(self, x, y):
        """Subtract Function"""
        return x - y


    def multiply(self, x, y):
        """Multiply Function"""
        return x * y


    def divide(self, x, y):
        """Divide Function"""
        # if y == 0:
        #     raise ValueError('Can not divide by zero!')
        return x / y

if __name__=='__main__':
    calc = Calculator()

    calc.info

    # Test cases
    print(f'Add(3, 4) >>> {calc.add(3, 4)}')
    print(f'subtract(3, 4) >>> {calc.subtract(3, 4)}')
    print(f'multiply(3, 4) >>> {calc.multiply(3, 4)}')
    print(f'divide(3, 4) >>> {calc.divide(3, 4)}')
