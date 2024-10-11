"""
    
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Example 1:

    Input: nums = [1,2,3,1]

    Output: true

    Explanation:

    The element 1 occurs at the indices 0 and 3.

    Example 2:

    Input: nums = [1,2,3,4]

    Output: false

    Explanation:

    All elements are distinct.

    Example 3:

    Input: nums = [1,1,1,3,3,4,3,2,4,2]

    Output: true

    

    Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
        
    
"""


def does_contain_duplicates_w_set(arr) -> bool:

    if len(arr) != len(set(arr)):
        return True
    return False


def does_contain_duplicates_w_dict(arr) -> bool:

    num_dict = dict()

    for num in arr:
        if num in num_dict.keys():
            return True
        else:
            num_dict[num] = 1

    return False


def does_contain_duplicates_w_list(arr) -> bool:

    sublist = []

    for num in arr:
        if num in sublist:
            return True
        else:
            sublist.append(num)

    return False


def does_contain_duplicates_w_sorted_list(arr) -> bool:

    sorted_list = sorted(arr)
    first_ptr = 0
    second_ptr = 1

    while second_ptr != len(sorted_list):
        if sorted_list[first_ptr] == sorted_list[second_ptr]:
            return True
        first_ptr += 1
        second_ptr += 1

    return False


if __name__ == "__main__":

    assert does_contain_duplicates_w_set([1, 2, 3, 1]) is True
    assert does_contain_duplicates_w_set([1, 2, 3, 4]) is False
    assert does_contain_duplicates_w_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

    assert does_contain_duplicates_w_dict([1, 2, 3, 1]) is True
    assert does_contain_duplicates_w_dict([1, 2, 3, 4]) is False
    assert does_contain_duplicates_w_dict([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

    assert does_contain_duplicates_w_list([1, 2, 3, 1]) is True
    assert does_contain_duplicates_w_list([1, 2, 3, 4]) is False
    assert does_contain_duplicates_w_list([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

    assert does_contain_duplicates_w_sorted_list([1, 2, 3, 1]) is True
    assert does_contain_duplicates_w_sorted_list([1, 2, 3, 4]) is False
    assert does_contain_duplicates_w_sorted_list([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert does_contain_duplicates_w_sorted_list([2, 3, 1, 1]) is True
