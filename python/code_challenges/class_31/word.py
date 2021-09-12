# from collections import Counter

from hash import HashTable

''''
Write a function called repeated word that finds the first word to occur more than once in a string
'''''
def repeatedWord(word):
    repeat=word.lower().split(" ")
    hash=HashTable()
    for  i in repeat:
        if hash.contains(i):
            return (i, len(repeat))
        hash.add(i,i)
    return "NO repeated word "
 
 

word  = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
print(repeatedWord( word ))
# Once upon a time, there was a brave princess who...
word  = "Once upon a time, there was a brave princess who..."
print(repeatedWord( word ))