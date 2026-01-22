def bubble_sort(nums: list):
    l = len(nums)
    for idx in range(l):
        swapped = False
        for jdx in range(0, l - idx - 1):
            if nums[jdx] > nums[jdx + 1]:
                nums[jdx], nums[jdx + 1] = nums[jdx + 1], nums[jdx]
                swapped = True
        if not swapped:
            return
    return


nums = [4, 1, 10, -10, -3, 20, 100, 34, -1000]
print(f"До сортировки: {nums}")
bubble_sort(nums)
print(f"После сортировки: {nums}")
