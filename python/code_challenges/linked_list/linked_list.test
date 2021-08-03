import pytest
from linked_list.linked_list import *


def test_insert(list_test):
    excpected = "10 -> 1 -> 0 -> None -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    inputs = [55,"Manar",10]
    actual = [list_test.includes(ele) for ele in inputs]
    excpected = [False, False , True]
    assert excpected == actual

def test_append(new_list):

    excpected = "1 -> 3 -> 2 -> 5 -> NULL"
    new_list.append(5)
    actual = f"{new_list}"
    assert excpected == actual
  
def test_insertAfter(new_list):
 
    excpected = "1 -> 3 -> 5 -> 2 -> NULL"
    new_list.insertAfter(3,5)
    actual = f"{new_list}"
    assert excpected == actual

def test_insertAfter1(new_list):

    excpected = "1 -> 3 -> 2 -> 5 -> NULL"
    new_list.insertAfter(2, 5)
    actual = f"{new_list}"
    assert excpected == actual

def test_insertAfter2():

    new_list = LinkedList()
    new_list.append(1)
    new_list.append(2)
    new_list.append(2)
    excpected = "1 -> 2 -> 5 -> 2 -> NULL"
    new_list.insertAfter(2,5)
    actual = f"{new_list}"
    assert excpected == actual

def test_insertAfter3(new_list):
    assert new_list.insertAfter(4,5) ==  None

def test_insertBefore1(new_list):

    excpected = "1 -> 5 -> 3 -> 2 -> NULL"
    new_list.insertBefore(3,5)
    actual = f"{new_list}"
    assert excpected == actual

def test_insertBefore2(new_list):

    excpected = "5 -> 1 -> 3 -> 2 -> NULL"
    new_list.insertBefore(1, 5)
    actual = f"{new_list}"
    assert excpected == actual

def test_insertBefore3():

    new_list = LinkedList()
    new_list.append(1)
    new_list.append(2)
    new_list.append(2)
    excpected = "1 -> 5 -> 2 -> 2 -> NULL"
    new_list.insertBefore(2,5)
    actual = f"{new_list}"
    assert excpected == actual

def test_insertBefore4(new_list):
    assert new_list.insertBefore(4,5) ==  None


def test_kthFromEnd(linked,new_list,list_of_kths):

    actual = [linked.kthFromEnd(i) for i in list_of_kths]
    expected = ['IndexError',1,'IndexError',3 , 2 ]
    assert actual == expected
def test_kthFromEnd2(linked):

    linked.append(1)
    actual = linked.kthFromEnd(0)
    expected = 1
    assert actual == expected
    assert linked.length() == 1


@pytest.fixture
def linked():
    return LinkedList()

@pytest.fixture
def list_of_kths():
    return [-1, 2, 3, 1, 0]

@pytest.fixture
def list_test(linked):
    linked.insert()
    linked.insert(0)
    linked.insert(1)
    linked.insert(10)
    return linked

@pytest.fixture
def new_list(linked):
    linked.append(1)
    linked.append(3)
    linked.append(2)
    return linked


