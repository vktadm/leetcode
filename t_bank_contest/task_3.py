from math import floor


class Solution:
    def solve(self, data_in):
        n, t = map(int, data_in[0].split())
        fl_n = list(map(int, data_in[1].split()))
        n_target = int(data_in[2])

        r_diff = fl_n[n - 1] - fl_n[n_target - 1]
        l_diff = fl_n[n_target - 1] - fl_n[0]
        rez = None

        if l_diff < t or r_diff < t:
            rez = fl_n[n - 1] - fl_n[0]

        if not rez:
            if l_diff <= r_diff:
                rez = l_diff * 2 + r_diff
            else:
                rez = r_diff * 2 + l_diff
        print(rez)


if __name__ == '__main__':
    s = Solution()
    s.solve(['5  5', '1  4  9  16  25', '2'])
    s.solve(['6  4', '1  2  3  6  8  25', '5'])
    s.solve(['6  1', '1  2  5  6  14  25', '5'])