from series_py import __version__
from series_py.series import fibonacci,lucas,sum_series


def test_version():
    assert __version__ == '0.1.0'
  


def test_fibonacci():
    expected = 3
    
    actual = fibonacci(4)
    
    assert expected == actual
  
  
def test_fibonacci_negative():
    expected = 'invalid value'
    
    actual = fibonacci(-1)
    
    assert expected == actual


def test_fibonacci_zero():
    expected = 0
    
    actual = fibonacci(0)
    
    assert expected == actual
    
    
def test_lucas():
    expected = 2
    
    actual = lucas(0)
    
    assert expected == actual


def test_lucas_negative():
    expected = 'invalid value'
    
    actual = lucas(-1)
    
    assert expected == actual
    
def test_lucas_zero():
    expected = 2
    
    actual = lucas(0)
    
    assert expected == actual    
    

    
def sum_series_3():
    expected = 2
    
    actual = sum_series(3)
    
    assert expected == actual

def sum_series_optional():
    expected = 7
    
    actual = sum_series(3,3,2)
    
    assert expected == actual
    
    
    