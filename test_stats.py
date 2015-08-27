from stats import mean

def test_mean():
        assert(mean([2,4]) == 3)
test_mean() 

def test_float_mean():
        assert(mean([2,3]) == 2.5)

test_float_mean()
