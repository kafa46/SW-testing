from math import pi

def circle_area(radius: float) -> float:
    '''compute circle area with given radius 'r' '''

    return pi * (radius**2)


if __name__=='__main__':

    # Test scenario
    test_input = [2, 0, -3, 2 + 5j, True, '123']
    MESSAGE = 'Area of circle with radius {radius} is {area}'
    for r in test_input:
        print(MESSAGE.format(radius=r, area=circle_area(r)))
