def partion(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[j], array[i] = array[i], array[j]
    i+=1
    array[i], array[r] = array[r], array[i]
    return i

def quickSort(array, p, r):
    if p < r:
        q = partion(array, p, r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)

if __name__ == '__main__':
    array = [-1, 0, -4, 1, 2, -1, -4]
    #array =  [12, 2, 14, 18, 3, 20, 22, 4, 5, 1, 6, 8, 9, 31, 10, 13, 101, 102, 103, 104, 107, 108, 1011, 1012, 1013, 1014, 1018, 1020, 1022]
    quickSort(array, 0, len(array)-1)
    print array