number = 12
dict = {}

try:
    dict = {'Apple'}
except TypeError:
    print ('typerror raised')
except KeyError:
    print('keyerror raised')
finally:
    print('exiting the try block')