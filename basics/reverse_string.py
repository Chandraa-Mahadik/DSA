# The Question: Write a Python function to reverse a string in Python using various methods, most notably the efficient and concise slicing method ([::-1]). 

input_str = "asdfghj"

def reverse_stray(str):
    """
    Returns a new string which is the reverse of s.
    Time:  O(n)
    Space: O(n)
    """
    str = list(str)

    left = 0
    right = len(str) - 1

    while left < right:
        # Swap the elements at left and right
        str[left], str[right] = str[right], str[left]

        left += 1
        right -= 1

    return "".join(str)


str_list = list(input_str)
print(reverse_stray(input_str))