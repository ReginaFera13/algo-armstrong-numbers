from armstrong_numbers import find_armstrong_numbers
import pytest 

def test_find_armstrong_numbers():
    assert find_armstrong_numbers([0]) == [0]
    assert find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7]
    assert find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    
    
# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
