# Reverse Only Letters Given a string that contains letters and non-letters, reverse only the letters, keeping non-letter characters in their original positions.
# "a-bC-dEf-ghIj" → "j-Ih-gfE-dCba"

def reverse_only_letters(s):
    """
    Reverses only the letters in the string 's'.
    Non-letter characters remain in their original positions.
    Time:  O(n)
    Space: O(n)  # uses a list for manipulation
    """

    s_list = list(s)
    left = 0
    right = len(s_list) - 1

    # Two-pointer approach
    while left < right:
        # Move left pointer until it hits a letter
        if not s_list[left].isalpha():
            left += 1
            continue

        # Move right pointer until it hits a letter
        if not s_list[right].isalpha():
            right -= 1
            continue

        # Swap letters
        s_list[left], s_list[right] = s_list[right], s_list[left]

        left += 1
        right -= 1

    return "".join(s_list)




print(reverse_only_letters("a-bC-dEf-ghIj"))  # "j-Ih-gfE-dCba"
