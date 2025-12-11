# Reverse String II (Patterned) Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string. 
# Example: s = "abcdefg", k = 2 → "bacdfeg"

def reverse_str_ii(s, k):
    """
    For every 2k characters in string 's',
    reverse the first k characters.
    Time:  O(n)
    Space: O(n)  # due to list conversion
    """

    s_list = list(s)

    # Process in chunks of size 2k
    for i in range(0, len(s_list), 2 * k):
        left = i
        right = min(i + k - 1, len(s_list) - 1)

        # Reverse only the first k characters in each 2k block
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            left += 1
            right -= 1

    return "".join(s_list)


print(reverse_str_ii("abcdefg", 2))  # "bacdfeg"

