def maxheap(a, n, i):
    largest = i         
    left = 2 * i + 1    
    right = 2 * i + 2   

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxheap(a, n, largest)


def heap_sort(a):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        maxheap(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]   
        maxheap(a, i, 0)  

    return a

a = [64, 28, 120, 32, 11]
print("Original Array:", a)

s_a = heap_sort(a.copy())

print("Sorted Array:", s_a)
