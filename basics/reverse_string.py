# The Question: Write a Python function to reverse a string in Python using various methods, most notably the efficient and concise slicing method ([::-1]). 

input_str = "asdfghj"

def reverse_stray(str):
    left = 0
    right = len(str) - 1

    while left < right:
        str[left], str[right] = str[right], str[left]

        left += 1
        right -= 1

    return str


str_list = list(input_str)
print("".join(reverse_stray(str_list)))