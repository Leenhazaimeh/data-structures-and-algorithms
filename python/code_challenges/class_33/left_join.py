from hash import*

def left_join(hash_map1,hash_map2):

    join_arr= []
    for hash in hash_map1._buckets:
        if hash != None:
            current = hash.head
            while current:
                join_arr+= [[current.value[0], current.value[1]],]
                current = current.next

    for hash in join_arr:

        if hash_map2.contains(hash[0]) == True:
            val = hash_map2.git(hash[0])
            hash.append(val)
        else:
            hash.append(None)

    return join_arr

test = Hashtable()
test.add('fond', '1')
test.add('wrath', '2')
test.add('diligent', '3')
test2 = Hashtable()
test2.add('fond', '3')
test2.add('wrath', '2')
test2.add('diligent', '1')

print(left_join(test,test2))