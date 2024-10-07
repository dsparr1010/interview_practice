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


if __name__ == "__main__":

    print(two_sum(arr=arr2, target=target2))
