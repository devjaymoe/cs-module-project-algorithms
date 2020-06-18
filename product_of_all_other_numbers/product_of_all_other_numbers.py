'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    products = [0 for i in range(len(arr))]
    multiplier = 1
    
    # first pass goes over the answer key and places a multiplier
    # the multiplier starts at 1 so that it will not overwrite the current index
    # on this first pass
    # it then captures the value at that index and places it in the multiplier
    # it goes onto the next index and multiplies at that index with the previous value's index
    for x in range(len(arr)):
        products[x] = multiplier
        multiplier *= arr[x]

    # reset the multiplier so that we skip the initial value
    multiplier = 1
    # the second pass goes in reverse and does the inverse of the first pass
    # to handle the multipler for the remaining values at each index in the 
    # answer key
    for y in range(len(arr) - 1, -1, -1):
        products[y] *= multiplier
        multiplier *= arr[y]

    return products

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [3, 7, 6, 4, 2]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
