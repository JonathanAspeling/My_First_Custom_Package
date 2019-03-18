def sum_array(array):

    '''Return sum of all integer items in array'''

    #Recursive sum, slices the array passed in from user n amount of times until only only one 
    #Element is left. Algorythm isolates each element of the array and sums it back together.
    if len(array) ==1:
        return array[0]
    else:
        return array[0]+sum_array(array[1:])


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

        

def factorial(n):

    '''Return n!'''
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


def reverse(word):

    '''Return word in reverse'''
    if len(word) == 1:
        return word[0]
    else:
        return word[-1]+reverse(word[0:-1])

