import pytest
from linked_list import *




def test_linkedlist():
    assert LinkedList()



def test_insert():
  
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(5)
    actual = ll.head.value
    assert actual == 5


def test_if_head_is_head():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(45)

    current=test.head
    current=current.next
    while current:
        if current.next==test.head:
            assert False
        else:
            current=current.next
    return False






def test_inserting_more():
    expected="45 -> 55 -> 66 -> NULL"
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    actual=test.__str__()
    assert actual==expected


def test_true_includes():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    actual=test.includes(55)
    assert actual==True

def test_false_includes():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    actual=test.includes(555)
    assert actual==False



def test_all_values_property():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    if ((66 in test.values) and(55 in test.values) and(45 in test.values)):
        assert True
    else:
        assert False


def test_append():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.appendvalue(77)
    expected="45 -> 55 -> 66 -> 77 -> NULL"
    actual=test.__str__()
    assert actual==expected


def test_multi_append():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.appendvalue(77)
    test.appendvalue(88)
    expected="45 -> 55 -> 66 -> 77 -> 88 -> NULL"
    actual=test.__str__()
    assert actual==expected


def test_insert_befor():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_befor(55,50)
    expected="45 -> 50 -> 55 -> 66 -> NULL"
    actual=test.__str__()
    assert actual==expected



def test_first_insert():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_befor(45,50)
    expected="50 -> 45 -> 55 -> 66 -> NULL"
    actual=test.__str__()
    assert actual==expected


def test_insert_after():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_after(55,50)
    expected="45 -> 55 -> 50 -> 66 -> NULL"
    actual=test.__str__()
    assert actual==expected



def test_insert_after_last():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert_after(66,50)
    expected="45 -> 55 -> 66 -> 50 -> NULL"
    actual=test.__str__()
    assert actual==expected




def test_kth_from_end():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    test.insert(30)
    test.insert(25)
    test.insert(20)
    test.insert(15)
    test.insert(10)
    
    expected=35
    actual=test.kth_from_end(3)
    assert actual==expected



def test_kth_same_length():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    expected='the k value is the same as the length of the list, please change it'
    actual=test.kth_from_end(4)
    assert actual==expected


def test_kth_is_negative():
    test=LinkedList()
    test.insert(66)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    expected='k is negative, please enter a positive number'
    actual=test.kth_from_end(-1)
    assert actual==expected


def test_kth_when_list_length_equal_one():
    test=LinkedList()
    test.insert(66)
    expected=66
    actual=test.kth_from_end(0)
    assert actual==expected


def test_kth_where_k_is_in_the_middle():
    test=LinkedList()
    test.insert(66)
    test.insert(60)
    test.insert(55)
    test.insert(45)
    test.insert(35)
    expected=55
    actual=test.kth_from_end(2)
    assert actual==expected


