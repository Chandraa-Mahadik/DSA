# Reverse Subarray
# Given an array and two indices l and r, reverse the elements only between l and r (inclusive).

# [1, 2, 3, 4, 5, 6], l=1, r=4 → [1, 5, 4, 3, 2, 6]

input_arr = [1,2,3,4,5,6]
l=1
r=4

def reverse_subarray(arr, l, r):
    """
    Reverses the list 'arr' in-place.
    Modifies the original list. Returns None.
    Time:  O(n)         # but effectively O(r - l)
    Space: O(1) 
    """

    left = l
    right = r

    while left < right:
        # Swap the elements at left and right
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr

print(reverse_subarray(input_arr, l, r))