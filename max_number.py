def find_max(numbers):
    if not numbers:
        return None  # or raise an error if empty list shouldn't be allowed
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([3, 7, 2, 8, 5]))
print(find_max([1, 1, 1, 1, 1]))
print(find_max([10, 20, 30, 5]))