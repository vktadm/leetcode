import unittest

import pandas as pd
from pandas._testing import assert_frame_equal


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    """Write a solution to calculate the number of bank accounts for each salary category."""
    return pd.DataFrame(
        {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count": [
                accounts[accounts.income < 20000].shape[0],
                accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[
                    0
                ],
                accounts[accounts.income > 50000].shape[0],
            ],
        }
    )


class TestCases(unittest.TestCase):
    def test_count_salary_categories(self):
        df = pd.DataFrame(
            {
                "account_id": [3, 2, 8, 6],
                "income": [108939, 12747, 87709, 91796],
            }
        )
        result = count_salary_categories(df)
        expected = pd.DataFrame(
            {
                "category": ["Low Salary", "Average Salary", "High Salary"],
                "accounts_count": [1, 0, 3],
            }
        )

        assert_frame_equal(result, expected)
