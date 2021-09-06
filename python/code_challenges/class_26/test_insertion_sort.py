from insertion_sort import insertion_sort



def test_inser3():
    data = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(data)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_sort2():
    data = [20, 18, 12, 8, 5, -2]
    actual = insertion_sort(data)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_sort3 ():
    data = [5, 12, 7, 5, 5, 7]
    actual = insertion_sort(data)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sort4():
    data = [2, 3, 5, 7, 13, 11]
    actual = insertion_sort(data)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected