#

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(0, len(items)-1):
        for o in range(0,len(items)-1-i):
            if items[o]>items[o+1]:
                items[o],items[o+1] = items[o+1], items[o]
    return items        


def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items

    items_half_index = len(items)//2
    items_left = merge_sort(items[:items_half_index])
    items_right = merge_sort(items[items_half_index:])

    return merge(items_left,items_right)


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:] if x < items[0]]) + [items[0]] + quick_sort([x for x in items[1:] if x >= items[0]])

