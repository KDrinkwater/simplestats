from stats import mean, std
from nose.tools import assert_equal, assert_almost_equal



def test_mean():
        assert_equal(mean([2,4]), 3)
#test_mean() 

def test_float_mean():
        assert_equal(mean([2,3]), 2.5)

#test_float_mean()

def test_negs():
	assert_equal(mean([-2,-4]), -3)
#test_negs()

def test_float():
	assert(mean([2.0,4.0]) == 3)
#test_float()

def test_std1():
	obs = std([0.0,2.0])
	exp = 1.0
	assert_equal(obs,exp)
