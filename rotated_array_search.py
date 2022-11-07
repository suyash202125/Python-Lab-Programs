def rotated_search(arr, t):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = start + (end - start)//2

        if t == arr[mid]:
            return mid

        if arr[start] <= arr[mid]:
            if t < arr[mid] and t >= arr[start]: 
                end = mid - 1
            else:
                start = mid + 1
        else:
            if t > arr[mid] and t <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return None
    

arr = [10, 13, 31, 39, 2, 4, 6, 8]
t = int(input("Enter the target element: "))
print(f"The index at which the target element {t} is", rotated_search(arr, t))