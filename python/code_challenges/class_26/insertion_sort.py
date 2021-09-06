def Inser_Sort(data):
    for i in range(1, len(data)):
        j = i - 1
        sort = data[i]

        while j >= 0 and sort < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        data[j+1] = sort


arr_a= [8,4,23,42,16,15]
arr_b = [20,18,12,8,5,-2]
arr_c = [5,12,7,5,5,7]
arr_d = [2,3,5,7,13,11]
if __name__=="__main__":
    Inser_Sort(arr_a)
    Inser_Sort(arr_b )
    Inser_Sort(arr_c)
    Inser_Sort(arr_d)
    print(arr_a)
    print(arr_b )
    print(arr_c)
    print(arr_d)

