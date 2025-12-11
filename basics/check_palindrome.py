# Write a Python function that checks whether a given string is a palindrome by reversing the string.
# A palindrome reads the same forward and backward.

# Examples:

# "racecar" → True

# "hello" → False

def is_palindrome(s: str) -> bool:
    """
    Checks whether the string 's' is a palindrome using two pointers.
    Returns True if it reads the same forward and backward.
    Time:  O(n)
    Space: O(1)
    """
        
    arr = list(s)

    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

print(is_palindrome("racecar"))
