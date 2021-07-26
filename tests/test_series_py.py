from series_py import __version__
from series_py.series import fibonacci,lucas,sum_series


def test_version():
    assert __version__ == '0.1.0'
  

# test fibonacci function by passing a normal number bigerr than zero
def test_fibonacci():
    expected = 3
    
    actual = fibonacci(4)
    
    assert expected == actual
  
# test fibonacci function by passing a negative number 
  
def test_fibonacci_negative():
    expected = 'invalid value'
    
    actual = fibonacci(-1)
    
    assert expected == actual

# test fibonacci function by passing a zero

def test_fibonacci_zero():
    expected = 0
    
    actual = fibonacci(0)
    
    assert expected == actual
    
# test lucas function by passing a normal number bigerr than zero
    
def test_lucas():
    expected = 1
    
    actual = lucas(1)
    
    assert expected == actual

# test lucas function by passing a negative number 

def test_lucas_negative():
    expected = 'invalid value'
    
    actual = lucas(-1)
    
    assert expected == actual
    
# test lucas function by passing a zero
    
def test_lucas_zero():
    expected = 2
    
    actual = lucas(0)
    
    assert expected == actual    
    

# test sum_series function by passing a the required parameter only
    
def test_sum_series():
    expected = 2
    
    actual = sum_series(3)
    
    assert expected == actual
    
# test sum_series function by passing a the required parameter with the two optional parameters as 2 , 1.
 
def test_sum_series_optional():
    expected = 4
    
    actual = sum_series(3,2,1)
    
    assert expected == actual
    
          
# test sum_series function by passing a the required parameter with the two optional parameters.

def test_sum_series_optional():
    expected = 7
    
    actual = sum_series(3,3,2)
    
    assert expected == actual
    
    
