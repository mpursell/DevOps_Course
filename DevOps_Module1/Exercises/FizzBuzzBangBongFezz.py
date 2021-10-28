import re

def checkFactors(num):

    # function to return the number of factors of a number and the factors themselves
    # returns a tuple where [0] is the number of factors and [1] is the list of factors

    # get the range of numbers we need (plus 1 since Python doesn't count
    # the last number in the range)
    countingRange = range(1,(num + 1))
    factorList  = []

    for countNumber in countingRange:
        factor = num % countNumber
        if factor == 0:
            factorList.append(countNumber) 

    numberOfFactors  = len(factorList)

    #print ('There are ' + numberOfFactors + ' factors of ' + str(num))
    #for result in factorList:
    #     print(result)

    return (numberOfFactors, factorList)

#checkFactors(13)[1]

def fizzBuzzBangBongFezz(startNumber, endNumber):

    # set the range and instantiate a dict with number=number key / value
    # for the given range
    numbersRange = range(startNumber, endNumber)
    numbersDict = {}

    # strings for printing

    str_three_and_five = 'FizzBuzz'
    str_three = 'Fizz'
    str_five = 'Buzz'
    str_seven = 'Bang'
    str_eleven = 'Bong'
    str_thirteen = 'Fezz'    


    # setup dict with {1:1, 2:2, 3:3...etc}
    for num in numbersRange:
        numbersDict.update({num:''})

    # update the dictionary with FizzBuzz / Bang / Bong ruleset
    for num in numbersRange:


        if (3 in checkFactors(num)[1]) and (5 in checkFactors(num)[1]):
            numbersDict.update({num:'FizzBuzz'})
            if (7 in checkFactors(num)[1]):
                numbersDict.update({num:'FizzBuzz' + 'Bang'})

        elif (11 in checkFactors(num)[1]):
            numbersDict.update({num:'Bong'})

        elif (3 in checkFactors(num)[1]):
            numbersDict.update({num:'Fizz'})
            if (7 in checkFactors(num)[1]):
                numbersDict.update({num:'Fizz' + 'Bang'})

        elif (5 in checkFactors(num)[1]):
            numbersDict.update({num:'Buzz'})
            if (7 in checkFactors(num)[1]):
                numbersDict.update({num: 'Buzz' + 'Bang'})
        
        elif (7 in checkFactors(num)[1]):
            numbersDict.update({num:'Bang'})

    
    # second pass over the dictionary to update with Fezz / reverse rules

    for num in numbersRange:

        # check if 13 is in the factor list, and the factor list is only 2
        # in length - that is the number is only divisible by 13 and 1
        if (13 in checkFactors(num)[1]) and (checkFactors(num)[0] == 2):
            strDictValue = numbersDict[num]
            numbersDict.update({num:'Fezz'})

        elif (13 in checkFactors(num)[1]):
            strDictValue = str(numbersDict[num])
            numbersDict.update({num:'Fezz' + strDictValue})

        elif(17 in checkFactors(num)[1]):

            # get the value of the key {num} as a string
            strDictValue = str(numbersDict[num])

            # spilt on capital letters into a list
            strDictValueList = re.findall('[A-Z][^A-Z]*', strDictValue)
            
            # reverse the list
            strDictValueList.reverse()
            
            # join the list elements into a string again
            strDictValue = "".join(strDictValueList)

            numbersDict.update({num:strDictValue})











        #if checkFactor(3, num) == 0  and checkFactor(7, num) == 0:
            
        #elif checkFactor(5, num) == 0 and checkFactor(7, num) == 0:
         #   numbersDict.update({num:'BuzzBang'})
        #elif checkFactor(3, num) == 0 and checkFactor(5, num) == 0:
        #    numbersDict.update({num:'FizzBuzz '})
    
        # check if number is also a multiple of 11, if it isn't print as per this
        # elif statement, otherwise we want to allow number to fall through to 
        # "Bong" condition
        #elif checkFactor(3, num) == 0 and checkFactor(11, num) != 0:
            #numbersDict.update({num:'Fizz'})
        #elif checkFactor(5, num) == 0 and checkFactor(11, num) != 0:
          #  numbersDict.update({num:'Buzz'})
        #elif checkFactor(7, num) == 0 and checkFactor(11, num) != 0:
           # numbersDict.update({num:'Bang'})
        #elif checkFactor(11, num) == 0:
           # numbersDict.update({num:'Bong'})
        
    
    
    # iterate over the dictionary with the previous ruleset and check:
    #  1. if the key is a multiple of 13, string add / replace to the value with "Fezz"
    #   in front of the first 'B'
    #  2. if the key is a multiple of 17, string split on capital letters and reverse
    #   word order
    #for numbersDictKey, numbersDictValue in numbersDict.items():
        
     #   if checkFactor(13, numbersDictKey) == 0:
      #      numbersDict.update({numbersDictKey:'Fezz'})
        
        
    # print out the key -> value pairs
    for numbersDictKey, numbersDictValue in numbersDict.items():

        print(numbersDictKey, numbersDictValue)

fizzBuzzBangBongFezz(1,256)