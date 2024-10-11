"""
    
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

    

    Example 1:

    Input: s = "anagram", t = "nagaram"

    Output: true

    Example 2:

    Input: s = "rat", t = "car"

    Output: false

    

    Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

        
"""

"""
Approach 1: sort and compare

- Sort string s and string t
- check if the sorted strings equal each other

- Complexity:
    - Time: O(n) (or O(2n)) because sorted uses a loop in the background
    - Space: O(n) because sorted returns a new list

"""


from collections import Counter


def is_anagram_w_sorted(s, t):
    s_sorted = sorted(s)
    t_sorted = sorted(t)

    return s_sorted == t_sorted


def is_anagram_w_counter(s, t):
    s_counter = Counter(s)
    t_counter = Counter(t)

    return s_counter == t_counter


if __name__ == "__main__":
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    assert is_anagram_w_sorted(s1, t1) is True
    assert is_anagram_w_sorted(s2, t2) is False

    assert is_anagram_w_counter(s1, t1) is True
    assert is_anagram_w_counter(s2, t2) is False
