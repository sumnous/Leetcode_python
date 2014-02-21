def partion(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] < x:
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
    array = [-1, 0, 1, 2, -1, -4]
    quickSort(array, 0, len(array)-1)
    print array