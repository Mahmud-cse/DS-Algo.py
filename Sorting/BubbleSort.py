def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


arr = [2, 6, 1, 7, 3]
bubbleSort(arr)

# Time Complexity:: O(n^2)
# Space Complexity:: O(1)