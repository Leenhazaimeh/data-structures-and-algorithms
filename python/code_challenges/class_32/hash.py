class HashTable:

    def __init__(self, lingth = 401):
        self._buckets = [None] *lingth 
        self.lingth  = lingth 
        
    def add(self,key,value):
        '''add a value to the hashtable by its key
            parameters:
                key: a string
                value: any type
            Arrgument: key and value
            return: nothing
        '''

        index = self.hash(key)

        if not self._buckets[index]:
         self._buckets[index] = LinkedList()


        self._buckets[index].append([key,value])



    def git(self,key):
        """this function will search in the hashtable about the key and return the value
        parameters:
        key: a string
        return: the value
        """
        index = self.hash(key)
        if self._buckets[index]:
            cuur=self._buckets[index].head
            while cuur:
                if cuur.value[0]==key:
                    print(cuur.value[1])
                    return cuur.value[1]
                cuur=cuur.next
        else:
            return None

            






    def contains(self,key):
        """this function will check if the there is a value for the key
        parameters:
        key: a string
        return: a boolean
        """
        index=self.hash(key)
        if self.buckets[index]:
         return self.buckets[index].includes(key)
        else:
            return False

   

    def hash(self,key):
        """
        This function take an string and return index that represent where should the value be in the array
        Arg:string
        return: number that represent index
        Let a hash function H(x) maps the value x at the index x%9 in an Array
        """
        value=0
        for h in key:
            value += ord(h)
        index = value * 9 % self.lingth 
        return index