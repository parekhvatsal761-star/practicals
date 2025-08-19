def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]      
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
a = [66, 15, 42, 772, 1]
print("Original Array:", a)

insertion_sort(a)

print("Sorted Array:", a)
