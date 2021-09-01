
def Merge_sort(data):
    n = len(data)

    if n > 1:
        mid = n//2
        right = data[mid:]
        left = data[0:mid]
        Merge_sort(right)
        Merge_sort(left)
        
        sort (left, right, data)

def sort ( right,left,data):
    k = 0
    i = 0
    j = 0
   

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j +=  1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1


temp = [8,4,23,42,16,15]
Reverse_sorted= [20,18,12,8,5,-2]
Few_uniques= [5,12,7,5,5,7]
Nearly_sorted= [2,3,5,7,13,11]
Merge_sort(temp)
Merge_sort(Reverse_sorted)
Merge_sort(Few_uniques)
Merge_sort(Nearly_sorted)
print(temp)
print(Reverse_sorted)
print(Few_uniques)
print(Nearly_sorted)