def quick_Sort(data,right, left):
    if left < right:
        position = Partition(data, right, left)
        quick_Sort(data, left, position - 1)
        quick_Sort(data, position + 1, right)

def Partition(data, left, right):
    cinter = data[right]
    low = left - 1
    for i in range (left , right):
        if data[i] <= cinter:
            low += 1
            Swap(data, i, low)

    Swap(data, right, low + 1)
    return low + 1

def Swap(data, i, low):
    temp = data[i]
    data[i] = data[low]
    data[low] = temp


temp = [8,4,23,42,16,15]
Reverse_sorted= [20,18,12,8,5,-2]
Few_uniques= [5,12,7,5,5,7]
Nearly_sorted= [2,3,5,7,13,11]
quick_Sort(temp, 0 ,len(temp)-1)
quick_Sort(Reverse_sorted, 0 ,len(Reverse_sorted)-1)
quick_Sort(Few_uniques, 0 ,len(Few_uniques)-1)
quick_Sort(Nearly_sorted, 0 ,len(Nearly_sorted)-1)
print(temp)
print(Reverse_sorted)
print(Few_uniques)
print(Nearly_sorted)