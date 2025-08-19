def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]

a = [29, 76, 18, 32, 61]
print("Original Array:", a)

selection_sort(a)

print("Sorted Array:", a)
