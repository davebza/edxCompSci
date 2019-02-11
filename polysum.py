import math

def polysum(n, s):

    '''This function takes two args:

    n = number of polygon sides
    s = length of each side

    and calculates the sum of the area and the perimeter squared of this polygon, which is returned as float rounded
    to four decimal places'''


    #pi defined to a very precise number:
    pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286

    area = (.25 * n * s**2) / (math.tan(pi/n))
    perimeterSquared = ((n * s)**2)

    return round((area+perimeterSquared), 4)
