def func(lst, number):
    l = len(lst)
    start = 0
    end = 1

    while start <= l - 2 and lst[start] < number:
        while end <= l - 1 and lst[start] + lst[end] <= number:
            if lst[start] + lst[end] == number:
                return True
            end += 1
        start += 1
        end = start + 1

    return False


print(func([1, 2, 3, 4, 5], 6))
print(func([1, 2, 3, 4, 5], 10))
print(func([2, 4, 5, 8, 9, 12], 9))
