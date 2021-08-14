  
import pytest 
from stack_and_queue import *


def test_tests():

  assert 1 == 1


@pytest.fixture
def data():
  new_stack = Stack()

  return {'stack':new_stack}



def test_stack_pushing_one_element(data):
  data['stack'].push(1)
  actual = data['stack'].top.value
  expected = 1
  assert actual == expected



def test_stack_push_lots_of_values():
  test =Stack()
  test.push(1)
  test.push(2)
  test.push(3)
  assert test.top.value==3

def test_stack_pop_one_element(data):
    data['stack'].push(1)
    data['stack'].push(2)
    actual = data['stack'].pop()
    expected = 2
    assert expected == actual


def test_empty_after_pops():
  test =Stack()
  test.push(1)
  test.push(2)
  test.push(3)
  test.pop()
  test.pop()
  test.pop()
  assert test.top==None


def test_stack_peak():
  test =Stack()
  test.push(1)
  test.push(2)
  test.push(3)
  assert test.peek()==3



def test_stack_is_empty():
  stack = Stack()
  assert stack.is_empty()



def test_peek_empty_stack_raises_exception():
  check_stack = Stack()
  with pytest.raises(Exception, match ="empty stack" ):
    check_stack.peek()




def test_enqueue_from_queue():
  test=Queue()
  test.enqueue(1)
  assert test.front.value==1


def test_enqueue_more_then_one_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  assert test.front.value==1 and test.rear.value==2


def test_dequee_more_then_one_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  test.enqueue(3)
  test.dequeue()

  assert test.front.value==2



def test_peek_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  test.enqueue(3)
  
  assert test.peek()==1


def test_peek_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  test.enqueue(3)
  test.dequeue()
  test.dequeue()
  test.dequeue()
  assert test.rear==None and test.front==None



def test_empty_queue():
  test=Queue()
  assert test.is_empty()


def test_dequeue_from_empty_queue():
  test=Queue()
  with pytest.raises(Exception, match ="empty queue" ):
    test.dequeue()