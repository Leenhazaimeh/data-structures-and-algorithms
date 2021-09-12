from word import*
 


def test_one():
    word = "Once upon a time, there was a brave princess who..."
    actual = repeatedWord(word)
    expected = ('a', 10)
    assert actual == expected

def test_tow():
    word= "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeatedWord(word)
    expected = ('it', 120)
    assert actual == expected

def test_repeatedWord():
    string = "It was the best of times."
    actual = repeatedWord(string)
    expected = "NO repeated word "
    assert actual == expected

