import pytest
from brackets import*

def test_1():
  bra_group = "{[]{()}}"
  expected = True
  actual = validate_brackets(bra_group)
  assert expected == actual
  
def test_2():
  bra_group = "[{}{})(]"
  expected = False
  actual = validate_brackets(bra_group)
  assert expected == actual
  
def test_3():
  bra_group = "((()"
  expected = False
  actual = validate_brackets(bra_group)
  assert expected == actual