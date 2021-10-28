import re

def checkFactors(num):

    # function to return the number of factors of a number and the factors themselves
    # returns a tuple where [0] is the number of factors and [1] is the list of factors
    # e.g. (3, [1,3,5])
    # if only two factors return we know that the number can only divisible by itself and 1

    # get the range of numbers we need (plus 1 since Python doesn't count
    # the last number in the range)
    countingRange = range(1,(num + 1))
    factorList  = []

    for countNumber in countingRange:
        factor = num % countNumber
        if factor == 0:
            factorList.append(countNumber) 

    numberOfFactors  = len(factorList)

    return (numberOfFactors, factorList)



def fizzBuzzBangBongFezz(startNumber, endNumber):

    # set the range and instantiate a dict with number:'' key / value
    # for the given range
    numbersRange = range(startNumber, endNumber)
    numbersDict = {}

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

        # if 13 is a factor, but there are more than 2 factors, add 'Fezz' to the start
        ######  NEEDS TO DO STRING INSERT OF FEZZ AT FIRST B #########
        elif (13 in checkFactors(num)[1]):
            strDictValue = str(numbersDict[num])
            numbersDict.update({num:'Fezz' + strDictValue})


        # if a number has 17 as a factor, reverse the Fizz, Buzz, Bang
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
        
    # print out the key -> value pairs
    for numbersDictKey, numbersDictValue in numbersDict.items():

        print(numbersDictKey, numbersDictValue)

fizzBuzzBangBongFezz(1,256)