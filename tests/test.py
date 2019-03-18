from mypackage import recursion
def test_sum_array():
        ''' 
        Ensures that sum_array with recursion works.
        '''
        assert recursion.sum_array([5,4,3,2,1])==15,'incorrect'
        assert recursion.sum_array([10,100,1000,10000])==111101,'incorrect'
