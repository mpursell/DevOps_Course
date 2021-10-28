


def FizzBuzz(startNumber, endNumber):

    # set the range of numbers we need
    numbers = range(startNumber, endNumber)

    # iterate over the range
    for num in numbers:
        
        # check if the remainder when divided by both 3 and 5
        # is 0.  
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz' + '(' + str(num) + ')')
        # check remainder when divided by 3 and 5 seperately
        elif num % 3 == 0:
            print('Fizz' + '(' + str(num) + ')')
        elif num % 5 == 0:
            print('Buzz' + '(' + str(num) + ')')
        # just print the number if it's not divisible by 3 or 5
        else:
            print(num)


FizzBuzz(1,101)