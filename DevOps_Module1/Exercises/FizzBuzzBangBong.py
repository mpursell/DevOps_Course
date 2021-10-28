# FizzBuzz / Bang / Bong 

def checkFactor(factor,num):

    # function takes a factor and a number
    # and will return the remainder of the division

    result = num % factor
    return result



def fizzBuzzBangBong(startNumber, endNumber):

    # function takes a range of numbers to loop over
    # calls checkFactor to see if there is any remainder left over from 
    # dividing the number in the range by the factor, and prints either the
    # number or FizzBuzz /Bang / Bong accordingly

    numbers = range(startNumber, endNumber)

    for num in numbers:
        
        if checkFactor(3, num) == 0  and checkFactor(7, num) == 0:
            print('FizzBang ')
        elif checkFactor(5, num) == 0 and checkFactor(7, num) == 0:
            print('BuzzBang')
        elif checkFactor(3, num) == 0 and checkFactor(5, num) == 0:
            print('FizzBuzz ')
        # check if number is also a multiple of 11, if it isn't print as per this
        # elif statement, otherwise we want to allow number to fall through to 
        # "Bong" condition
        elif checkFactor(3, num) == 0 and checkFactor(11, num) != 0:
            print('Fizz')
        elif checkFactor(5, num) == 0 and checkFactor(11, num) != 0:
            print('Buzz')
        elif checkFactor(7, num) == 0 and checkFactor(11, num) != 0:
            print('Bang')
        elif checkFactor(11, num) == 0:
            print('Bong ')
        else:
            print(num)
    

fizzBuzzBangBong(1, 101)


