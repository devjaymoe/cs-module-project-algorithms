'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    numbers = []
    zeros = []
    # loop through array
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros.append(arr[i])
        else:
            numbers.append(arr[i])

    return numbers + zeros

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")