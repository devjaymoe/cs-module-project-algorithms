'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # go through the array
    aPointer = 0
    bPointer = aPointer + 1
    current = arr[aPointer]
    next_num = arr[bPointer]
    no_match_found = False
    # number has a match
    while no_match_found == False:
        # the number is found
        if current == next_num:
            # check if the current value is at the end of the list
            # if the two pointers are at the same spot then the number was not found
            if bPointer == aPointer:
                # make this the non-number found and end loop
                no_match_found = current
            elif aPointer == len(arr):
                # end the while loop since at the end of the array
                no_match_found = True
            # assign current number to the next item in the array
            else:
                # increment the current number
                aPointer += 1
                current = arr[aPointer]
                # increment the next number the the number following a
                bPointer = aPointer + 1
                next_num = arr[bPointer]
        # they do not match so check the next value
        else:
            # increment the next pointer's index
            bPointer += 1
            # check if pointer is at end of the list
            # if bPointer is at the end of the list reset the pointer
            if bPointer == len(arr) - 1:
                # reset the bPointer to the beginning
                bPointer = 0
                next_num = arr[bPointer]
            else:
                # increment the b pointer to check the next value
                # assign it to the next value
                next_num = arr[bPointer]
    return no_match_found


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")