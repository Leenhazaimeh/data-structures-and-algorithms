from quick_sort import quick_Sort

def test_insertion_sort():
    userinput = [8,4,23,42,16,15]
    expected = [4, 8, 15, 16, 23, 42]
    quick_Sort(userinput, 0 ,len(userinput)-1)
    assert userinput == expected

def test_insertionSort2():
    input = [20, 41, 3, 2, 16, 10]
    expected = [2, 3, 10, 16, 20, 41]
    quick_Sort(input, 0 ,len(input)-1)
    assert input == expected