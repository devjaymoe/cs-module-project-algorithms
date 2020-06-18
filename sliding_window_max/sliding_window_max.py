'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # answers = []
    # sub_Array = [0] * k
    # iterations = 0
    #
    # for i in range(len(nums) - k + 1):
    #     iterations = i
    #     sub_Array_index = 0
    #     sub_Array = [0] * k

    #     for sub_index in range(len(sub_Array)):
    #         sub_Array[sub_index] = nums[iterations]
    #         iterations += 1

    #     answers.append(max(sub_Array))

    # place the inital sub array with the first values in num with the length of k
    sub_Array = [nums[i] for i in range(k)]
    # find the max in this thing and add it to the answer array
    answers = []
    answers.append(max(sub_Array))

    # loop through the number array
    # stopping once the sub array is at the end of the nums list
    for index in range(len(nums) - len(sub_Array)):
        # pop the first index
        sub_Array.pop(0)
        # append to the sub array the value that the next value the sub array needs
        sub_Array.append(nums[index + k])
        # find the max value in this new sub array with the new value
        answers.append(max(sub_Array))

    return answers


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
