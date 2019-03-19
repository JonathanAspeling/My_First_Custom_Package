#

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(0, len(items)-1):
        for o in range(0,len(items)-1-i):
            if items[o]>items[o+1]:
                items[o],items[o+1] = items[o+1], items[o]
    return items        


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:] if x < items[0]]) + [items[0]] + quick_sort([x for x in items[1:] if x >= items[0]])

