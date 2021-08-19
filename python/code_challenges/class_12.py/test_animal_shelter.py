import pytest

from animal_shelter import *






@pytest.fixture
def animal():

    shelter=Animal_Shelter()

    boxser=Dog("boxser")
    kok=Dog('kok')
    mog=Dog('mog')

    luci=Cat("luci")
    nani=Cat("nani")
    rafial=Cat("rafial")

    shelter.enqueue(boxser)
    shelter.enqueue(kok)
    shelter.enqueue(mog)
    shelter.enqueue(luci)
    shelter.enqueue(nani)
    shelter.enqueue(rafial)

    return shelter



def test_shelter():
    assert Animal_Shelter()


def test_enqueue_values(animal):
   

    actual=animal.dogs.front.value.name
    actual2=animal.cats.front.value.name
    expected="boxser"
    expected2="luci"

    assert actual==expected
    assert actual2==expected2

def test_dequeue_data(animal):
   

    actual=animal.dequeue("dog")
    actual2=animal.dequeue("cat")
    expected="boxser"
    expected2="luci"

    assert actual.name==expected
    assert actual2.name==expected2


def test_if_none(animal):
   
    actual=animal.dequeue("bird")
    expected=None
    assert actual==expected