def length_of_longest_substring(s):
    char_map = {}
    max_length = start = 0
    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length
print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))     
