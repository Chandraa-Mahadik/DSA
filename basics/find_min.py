# Find Min in Array
# Return minimum element of array.

input_arr = [10,50,40,800,200, 2, 500]

def find_min(arr):
    if len(arr) == 0:
        return "arr is empty"
    else:
        min = arr[0]
        
        for i in range(1,len(arr) - 1):
            if min > arr[i]:
                min = arr[i]

        return min
    
print(find_min(input_arr))