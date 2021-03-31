def sort_k(arr, k):
    #print(sorted(arr, key=k))
    #for eacharr in array:
    #    print(eacharr)
    for row in sorted(arr, key=lambda row:row[k]):
        print(' '.join(map(str, row)))
k = 0
array = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
sort_k(array, k)