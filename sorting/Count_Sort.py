def count_sort(nums: list):
    if not nums:
        return nums

    min_val = min(nums)
    max_val = max(nums)
    count = [0] * (max_val - min_val + 1)

    for num in nums:
        count[num - min_val] += 1

    sorted_arr = []
    for num in range(len(count)):
        sorted_arr.extend([num + min_val] * count[num])

    return sorted_arr


nums = [1, 2, 3, 2, 3, 1, 3, 3, 3, 1, 1, 1, 1, 2, 3, 2, 2, 1, 1]
print(f"До сортировки: {nums}")
print(f"После сортировки: {count_sort(nums)}")
