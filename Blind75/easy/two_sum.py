"""
Solved w Brian on 10/4/24


"""

arr = [1, 2, 3, 3, 4, 6]
target = 7

arr2 = [1, 2]
target2 = 4


def two_sum(arr, target):

    if len(arr) == 1:
        return False

    for index, num in enumerate(arr):
        new_target = target - num

        for inner_index in range(index + 1, len(arr)):
            if arr[inner_index] == new_target:
                return True

    return False


def thing(arr):
    # Showing a way to start a loop at an index that isn't 0
    for index in range(1, len(arr)):
        print(arr[index])


# print(two_sum(arr=arr2, target=target2))
#  *.       *
# [2, 3, 5, 1, 9, 2, 3, 5]
# *.   *


def two_sum_ptrs(arr, target):
    first_ptr = 0
    second_ptr = len(arr) - 1
    sorted_list = sorted(arr)

    while first_ptr <= second_ptr:
        summed_value = sorted_list[first_ptr] + sorted_list[second_ptr]
        if summed_value == target:
            return True
        if summed_value < target:
            first_ptr += 1
        else:
            # summed_value > target:
            second_ptr -= 1

    return False

    #  *


arr3 = [3, 1]
target3 = 6

# if target - arr[i] is in seen:

# add curr num to set
# target = 6


def two_sum_w_set(arr, target):
    seen_numbs = set()
    # checking for complement in seen_numbs
    # adding seen values to set

    for num in arr:
        complement = target - num
        if complement in seen_numbs:
            return True
        seen_numbs.add(complement)

    return False


if __name__ == "__main__":

    print(two_sum(arr=arr2, target=target2))
    print(two_sum_w_set(arr3, target3))
