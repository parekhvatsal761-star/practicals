import time

def linear_search(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return i   
    return -1          

if __name__ == "__main__":
    a = [5, 8, 1, 3, 9, 6]
    target = 9
    print("Array:", a)
    print("Target:", target)

    start = time.time()
    index = linear_search(a, target)
    end = time.time()

    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")

    print("Time Taken :", end - start, "seconds")
