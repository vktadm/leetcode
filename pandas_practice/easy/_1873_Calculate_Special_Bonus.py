import unittest

import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (employees["employee_id"] % 2 != 0) & (employees["name"].str[0] != "M")
    bonus_series = condition.astype(int) * employees["salary"]
    result = employees.assign(bonus=bonus_series)[["employee_id", "bonus"]].sort_values(
        "employee_id"
    )
    return result


class CalculateSpecialBonusTest(unittest.TestCase):
    def test_calculate_special_bonus(self):
        data1 = {
            "employee_id": [2, 3, 7, 8, 9],
            "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
            "salary": [3000, 3800, 7400, 6100, 7700],
        }
        df1 = pd.DataFrame(data1)

        expected1 = pd.DataFrame(
            {"employee_id": [2, 3, 7, 8, 9], "bonus": [0, 0, 7400, 0, 7700]}
        )

        result1 = calculate_special_bonus(df1)
        pd.testing.assert_frame_equal(
            result1.reset_index(drop=True), expected1.reset_index(drop=True)
        )
