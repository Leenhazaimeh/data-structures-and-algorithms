class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    '''add a value to the hashtable by its key
            parameters:
            
                value: any type
            Arrgument: value
            return: nothing
        '''

    def add(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

class Hashtable:
    def __init__(self, lingth = 401):
        self._buckets = [None]*lingth
        self.lingth = lingth

    def hash(self, key):
        """
        This function take an string and return index that represent where should the value be in the array
        Arg:string
        return: number that represent index
        Let a hash function H(x) maps the value x at the index x%9 in an Array
        """
        total = 0
        for i in key:
            total += ord(i)
        return total*19 % self.lingth

    def add(self, key, value):
        h = self.hash(key)

        if self._buckets[h] == None:
            self._buckets[h] = LinkedList()
            self._buckets[h].add([key , value])

        if self.contains(key):
            current = self._buckets[h].head
            while current:
                if current.value[0] == key :
                    current.value[1] = value
                current = current.next

        else:
            self._buckets[h].add([key , value])


    def git(self, key):
        h = self.hash(key)
        if self._buckets[h]:
            current = self._buckets[h].head
            while current:
                if current.value[0] == key :
                    return current.value[1]
                current = current.next
            return 'key not exist'
        else:
            return 'key not exist'

    def contains(self, key):
        h = self.hash(key)
        if self._buckets[h]:
            current = self._buckets[h].head
            while current:
                if current.value[0] == key :
                    return True
                current = current.next
            return False
        else:
            return False