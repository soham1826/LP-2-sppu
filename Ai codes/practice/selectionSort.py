def selection(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if(arr[j] < arr[min_index]):
                min_index = j

        arr[i] ,arr[min_index] = arr[min_index] , arr[i]

        print("Iteration" ,i+1,":", arr)
    
    return arr


array = [10,23 ,2,18,22,56,1,45]
sorted_arr = selection(array)
print("selection sort of array is ", sorted_arr)