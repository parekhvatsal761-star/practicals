import time

def binary_search(a, target):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    a = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    print("Array:", a)
    print("Target:", target)

    start = time.time()
    index = binary_search(a, target)
    end = time.time()

    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found !!!")

    print("Time Taken :", end - start, "seconds")
