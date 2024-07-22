def product_except_self(nums):
    length = len(nums)
    result = [1] * length
    left = 1
    for i in range(length):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(length - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result
print(product_except_self([1,2,3,4]))  
