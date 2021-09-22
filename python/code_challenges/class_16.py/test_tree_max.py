import pytest
from tree_max import *





def test_MaxValue(root):
    actual = root.MaxValue()
    expected = 7
    assert actual == expected



