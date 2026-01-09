def longest_substring_length(s):
    last_seen = {}
    start = 0
    max_length = 0

    for i in range(len(s)):
        char = s[i]
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = i
        current_length = i - start + 1
        if current_length > max_length:
            max_length = current_length
    return max_length

if __name__ == "__main__":
    inputs = ["abcabcbb","bbbbb","","pwwkew","abcdef"]

    for value in inputs:
        print(f"The length of the longest substring without repeating characters in '{value}' is {longest_substring_length(value)}")