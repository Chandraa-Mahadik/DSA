# Find Max in Array
# Return maximum element of array.

input_arr = [10,50,40,800,200,500]

def find_max(arr):
    if len(arr) == 0:
        return "arr is empty"
    else:
        max = arr[0]
        
        for i in range(1,len(arr) - 1):
            if max < arr[i]:
                max = arr[i]

        return max
    
print(find_max(input_arr))
    