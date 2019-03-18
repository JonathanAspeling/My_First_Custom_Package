#

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(0, len(items)-1):
        for o in range(0,len(items)-1-i):
            if items[o]>items[o+1]:
                items[o],items[o+1] = items[o+1], items[o]
    return items        

print(bubble_sort([1,3,2,6,8,5]))

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
