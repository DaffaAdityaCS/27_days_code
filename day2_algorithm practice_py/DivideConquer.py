
def selectionsort(val):
    for i in range(len(val)):
        min_idx = i
        for j in range(i+1, len(val)):
            if val[min_idx] > val[j]:
                min_idx = j
       
        val[i], val[min_idx] = val[min_idx], val[i]
    
def BubbleSort(val, n):
    for i in range(n - 1):
        for j in range(n -i -1):
            if(val[j] > val[j+1]):
                temp = val[j]
                val[j] = val[j+1]
                val[j+1] = temp



def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def insertionSort(var):
    for i in range(1, len(var)-1):
        j = i
        while j > 0 and var[j-1] > var[j]:
            temp = var[j-1]
            var[j-1] = var[j]
            var [j] = temp
            j = j - 1


def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0     
    j = 0     
    k = l    
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 


