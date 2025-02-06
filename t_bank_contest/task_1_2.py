class Solution:
    def task1(self, s):
        a, b, c, d = map(int, s.split())
        # a - абонентская плата
        # b - кол-во мбайт трафика
        # с - каждый последующий мбайт трафика
        # d - кол-во мегабайт, которые Костя планирует потратить
        print(a + (c * (d - b)) if d > b else a)

    def task2(self, n):
        # n - кол-во кусочков рулета
        cuts = 0
        index = 0
        while n > 0:
            # Проверка, является ли последний бит единицей
            if n & 1:
                cuts += index if index != 0 else 1
            n >>= 1  # Сдвиг числа вправо на один бит
            index += 1
        print(cuts)

if __name__ == '__main__':
    s = Solution()
    # s.task1('100  10  12  15')
    # s.task1('100  10  12  1')
    s.task2(23)



