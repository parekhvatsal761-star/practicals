def bubble_sort(a):
    n = len(a)
    
    for i in range(n-1):
       
        for j in range(n-i-1):
            if a[j] > a[j+1]:
               
                a[j], a[j+1] = a[j+1], a[j]

a = [64, 25, 12, 22, 11]
print("Original Array:-", a)

bubble_sort(a)

print("Sorted Array:", a)
