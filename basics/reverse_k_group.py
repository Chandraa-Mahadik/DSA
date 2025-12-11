# K-Group Reversal on Array
# Given an array and an integer k, reverse the array in chunks of size k. For the last group, if the size is < k, keep it as is.
# Example :
# [1,2,3,4,5,6,7,8,9], k=3 → [3,2,1, 6,5,4, 7,8,9]

# (These start hinting at patterns used in more complex linked list problems.)

def reverse_k_group(arr, k):
    """
    Reverses the array 'arr' in groups of size k.
    If the last group has fewer than k elements, leave it as is.
    Time:  O(n)
    Space: O(1)
    """

    for i in range(0, len(arr), k):
        # Only reverse if a full k-group exists
        if i + k <= len(arr):
            left = i
            right = i + k - 1

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

    return arr


print(reverse_k_group([1,2,3,4,5,6,7,8,9], 3))