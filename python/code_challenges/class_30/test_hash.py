import pytest 
from hash_tabel import *



def test_hashtable():
    test=HashTable()
    test.add("hash",3333)
    test.add("tabel",4444)
    return test


def test_add():
  test=HashTable()
  test.add("map",5555)
  assert test.contains('map')==True

def test_hash():
  test=HashTable()
  assert  test.hash("leen")==700

def test_git(test_hashtable):
    test=test_hashtable
    assert test.git("hash")==3333
    assert test.git("tabel") ==4444

def test_not_git(test_hashtable):
    test=test_hashtable
    assert test.git("test") == None

def test_contains(test_hashtable):
    test=test_hashtable
    assert test.contains("hash")
    assert test.contains("tabel")

def test_retrieve():
    test=HashTable(3)
    test.add("map",5555)
    test.add("leen",7777)
    assert test.git("leen")==7777

   