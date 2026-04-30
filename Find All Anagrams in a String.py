from collections import Counter

def find_anagrams(s, p):
    result = []
    
    if len(p) > len(s):
        return result

    p_count = Counter(p)
    window_count = Counter()

    left = 0

    for right in range(len(s)):
        # Add current character to window
        window_count[s[right]] += 1

        # Maintain window size = len(p)
        if right - left + 1 > len(p):
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            left += 1

        # Compare both counts
        if window_count == p_count:
            result.append(left)

    return result
