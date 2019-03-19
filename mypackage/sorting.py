#

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(0, len(items)-1):
        for o in range(0,len(items)-1-i):
            if items[o]>items[o+1]:
                items[o],items[o+1] = items[o+1], items[o]
    return items        


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) < 2:
        return items
    result = []
    mid = int(len(items) / 2)
    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:] if x < items[0]]) + [items[0]] + quick_sort([x for x in items[1:] if x >= items[0]])

