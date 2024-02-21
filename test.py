from mypackage import myModule

def test_sum_n():
    """make sure sum_n works correctly
    """
    assert myModule.sum_n([3,2,5,9,6], 3) == 10, 'incorrect'
