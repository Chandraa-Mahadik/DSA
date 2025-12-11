# The Question: Write a Python function to reverse the elements of a given array (list) in-place without using any built-in reverse() method or slicing [::-1]. 

input_arr = [10,20,30,40,50]
input_str = "asdfghj"

def reverse_array(arr):
    """
    Reverses the list 'arr' in-place.
    Modifies the original list. Returns None.
    Time:  O(n)
    Space: O(1) extra
    """

    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap the elements at left and right
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


str_list = list(input_str)
print("".join(reverse_array(str_list)))
