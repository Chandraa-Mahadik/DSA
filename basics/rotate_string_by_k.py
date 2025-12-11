# String Rotation by Reversal You are given a string s and an integer k. Rotate the string to the right by k positions using only the reverse operation (you can reverse any substring in O(n)). 
# Example: s = "abcdef", k = 2 → "efabcd" 
# Hints: 
# Think of array rotation by reversal: 
    # Reverse whole string. 
    # Reverse first k characters. 
    # Reverse last n-k characters.
    
def rotate_string_by_k(s, k):
    """
    Rotates string 's' to the right by k using only reversal operations.
    (Approach: reverse whole string, reverse first k, reverse last n-k)
    Time:  O(n)
    Space: O(n)  # strings are immutable, so we use a list
    """

    n = len(s)
    k = k % n
    arr = list(s)

    # Helper reverse function
    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    # 1. Reverse entire string
    reverse(0, n - 1)

    # 2. Reverse first k characters
    reverse(0, k - 1)

    # 3. Reverse last n-k characters
    reverse(k, n - 1)

    return "".join(arr)


# Test
print(rotate_string_by_k("abcdef", 2))  # "efabcd"