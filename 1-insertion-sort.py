def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        # move elements before current to the right
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # placing current element to the begining
        arr[j+1] = key

def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

if __name__ == "__main__":
    arr = [5, 3 , 1, 9, 12, 4]
    insertion_sort_2(arr)
    print(arr)

