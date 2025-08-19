def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[len(a) // 2]   
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Main Program
a = [87, 625, 2, 21, 10]
print("Original Array:", a)

s_a = quick_sort(a)

print("Sorted Array:", s_a)
