# Задачи с собесов
***
##### Написать функцию, которая проверяет правильность строки по скобкам

- () - True
- (() - False
- ) - False
- ()()((((())))) - True

Более сложный случай, если скобки могут быть и фигурные и квадратные
```python
def isValid(s):
    p_map = {
            '}': '{',
            ')': '(',
            ']': '['
    }
    p_stack = []

    for value in s:
        if p_stack and value in p_map:
            pre_value = p_stack.pop()
            
            if pre_value != p_map[value]:
                return False
        else:
            p_stack.append(value)

    if len(p_stack):
        return False
    
    return True
```
##### Вычислить если такие два числа в упорядоченном списке, сумма которых равна числу (number)
- func([1,2,3,4,5], 6) --> True, тк сумма 2 и 4 
- func([1,2,3,4,5], 10) --> False, тк нет таких чисел
```python
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
```
##### Написать бесконечный счетчик counter(). Если передается число, то он ограничен
- for i in counter() -> 1,2,3,4,5,6,7,8,...
- for i in counter(5) -> 1,2,3,4,5
```python
def endless_counter(value=float('inf')):
    idx = 0
    while idx <= value:
        print(idx, end=', ' if idx != value else '.')
        idx += 1
```
