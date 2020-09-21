def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [left for left in data if left < pivot]
    right = [right for right in data if right > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


def longest_palindrome(s: str) -> str:
    if len(s) == 1:
        return s
    longest = ''
    for left in range(len(s)):
        for right in range(left, len(s) + 1):
            current = s[left:right]
            if is_palindrome(current) and right - left > len(longest):
                longest = s[left:right]
    return longest


def is_palindrome(s: str) -> bool:
    return s == s[::-1]
