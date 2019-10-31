def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)

def square_numbers_using_generators(nums):
    for i in nums:
        yield(i*i)

my_nums_using_generators = square_numbers_using_generators([1,2,3,4,5])

print(next(my_nums_using_generators))



## LIST COMPRESSION

my_num_list_compression = [x*x for x in [1,2,3,4,5]]

for num in my_num_list_compression:
    print(num)