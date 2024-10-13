# 1d candy crush. If you there are candies of the same type thats 3 in a row, we remove them.
# [1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 3]
# Output: [1, 2]


def candy_crush(candies):

    new_stack = []
    counter = {}

    for numb in candies:
        if numb in counter:
            counter[numb] += 1
        else:
            counter[numb] = 1

        print(new_stack)
        print(f"counter: {counter}")

        if len(new_stack) > 1:
            if numb != new_stack[-1]:
                last_number_added = counter[new_stack[-1]]
                if last_number_added >= 3:
                    for _ in range(last_number_added):
                        new_stack.pop()
                    print(f"new stack after removal: {new_stack}")
                    del counter[last_number_added]

            # if new_stack[-1] == numb and new_stack[-2] == numb:
            # if new_stack[counter] == numb:
            #   new_stack.pop()
            #   new_stack.pop()
        new_stack.append(numb)

    return new_stack


# print(candy_crush([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 3]))
# print(candy_crush([1, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 3]))
print(candy_crush([1, 2, 3, 5, 13, 3, 3, 4, 4, 4, 4, 3, 5, 5, 5, 3, 3, 5]))
