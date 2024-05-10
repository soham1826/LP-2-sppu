def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            # Find the index of the minimum element in the unsorted part of the array
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Print the array after each iteration
        print("Iteration", i+1, ":", arr)
    
    return arr


# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
