# Reverse Words in a Sentence
# Given a string with words separated by spaces, reverse the order of words but keep each word’s letters in order.

# "I love coding" → "coding love I"

def reverse_words(sentence):
    """
    Reverses the order of words in the given sentence.
    Keeps each word's characters in the same order.
    Time:  O(n)
    Space: O(n)  # due to splitting into a list
    """
    
    s_list = sentence.split(" ")
    
    left = 0
    right = len(s_list) - 1
    
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        
        left += 1
        right -= 1
        
    return " ".join(s_list)

print(reverse_words("I love coding"))