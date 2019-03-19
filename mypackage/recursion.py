def sum_array(array):

    '''Return sum of all integer items in array'''


    if len(array) ==1:
        return array[0]
    else:
        return array[0]+sum_array(array[1:])


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''


    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)



def factorial(n):

    '''Return n!'''

    
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


def reverse(word):

    '''Return word in reverse'''
    if len(word) == 1:
        return word[0]
    else:
        return word[-1]+reverse(word[0:-1])

