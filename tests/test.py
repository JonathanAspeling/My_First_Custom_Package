from mypackage import recursion
from mypackage import sorting
def test_sum_array():
        ''' 
        Ensures that sum_array with recursion works.
        '''
        assert recursion.sum_array([5,4,3,2,1])==15,'incorrect'
        assert recursion.sum_array([10,100,1000,10000])==11110,'incorrect'

def test_fibonacci():

        '''
        Ensures that fibonacci with recursion works.
        '''
        assert recursion.fibonacci(9)==34,'incorrect'
        assert recursion.fibonacci(10)==55,'incorrect'
        assert recursion.fibonacci(11)==89,'incorrect'

def test_factorial():

        '''
        Ensures that factorial works with recursion works.
        '''
        assert recursion.fibonacci(3)==6,'incorrect'
        assert recursion.fibonacci(4)==24,'incorrect'
        assert recursion.fibonacci(10)==3628800,'incorrect'

def test_reverse():

        '''
        Ensures that reverse function works with recursion works.
        '''
        assert recursion.reverse('Apple')=='elppA','incorrect'
        assert recursion.reverse('Doom')=='mooD','incorrect'
        assert recursion.reverse('Algea')=='aeglA','incorrect'

def test_bubble_sort():
        '''
        Ensures that buble_sort function works.
        '''

        assert sorting.bubble_sort([5,4,3,2,1])==[1,2,3,4,5],'incorrect'

def test_merge_sort():
        '''
        Ensures that merge_sort function works.
        '''
        assert sorting.merge_sort([5,4,3,2,1])==[1,2,3,4,5],'incorrect'

def test_quick_sort():
        '''
        Ensures that quick_sort function works.
        '''
        assert sorting.quick_sort([5,4,3,2,1])==[1,2,3,4,5],'incorrect'