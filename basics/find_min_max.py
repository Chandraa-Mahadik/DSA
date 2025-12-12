# Find Max and Min Together
# Write a function returning both using only 1 loop.


input_arr = [10,50,40,800,200,500]

def find_min_max(arr):
    if len(arr) == 0:
        return "arr is empty"
    else:
        min = arr[0]
        max = arr[0]
        
        for i in range(1,len(arr) - 1):
            if min > arr[i]:
                min = arr[i]
                
            if max < arr[i]:
                max = arr[i]

        return min, max
    
print(find_min_max(input_arr))


    