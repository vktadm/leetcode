import unittest

import pandas as pd


def sales_person(
    sales_person: pd.DataFrame,
    company: pd.DataFrame,
    orders: pd.DataFrame,
) -> pd.DataFrame:
    red_company = company.loc[company["name"] == "RED"]["com_id"]
    red_company = red_company.to_list()
    red_orders = orders.loc[orders["com_id"].isin(red_company)]["sales_id"]
    red_orders = red_orders.to_list()
    result = sales_person.loc[~sales_person["sales_id"].isin(red_orders)][["name"]]
    return result


class TestSalesPersonRedCompany(unittest.TestCase):
    def setUp(self):
        """Set up test data as pandas DataFrames matching the example"""
        self.sales_person_df = pd.DataFrame(
            {
                "sales_id": [1, 2, 3, 4, 5],
                "name": ["John", "Amy", "Mark", "Pam", "Alex"],
                "salary": [100000, 12000, 65000, 25000, 5000],
                "commission_rate": [6, 5, 12, 25, 10],
                "hire_date": [
                    "4/1/2006",
                    "5/1/2010",
                    "12/25/2008",
                    "1/1/2005",
                    "2/3/2007",
                ],
            }
        )

        self.company_df = pd.DataFrame(
            {
                "com_id": [1, 2, 3, 4],
                "name": ["RED", "ORANGE", "YELLOW", "GREEN"],
                "city": ["Boston", "New York", "Boston", "Austin"],
            }
        )

        self.orders_df = pd.DataFrame(
            {
                "order_id": [1, 2, 3, 4],
                "order_date": ["1/1/2014", "2/1/2014", "3/1/2014", "4/1/2014"],
                "com_id": [3, 4, 1, 1],
                "sales_id": [4, 5, 1, 4],
                "amount": [10000, 5000, 50000, 25000],
            }
        )

    def test_original_example(self):
        """Test with the exact data from the example"""
        expected_output = ["Amy", "Mark", "Alex"]
        expected_output_df = pd.DataFrame(expected_output, columns=["name"])
        result = sales_person(self.sales_person_df, self.company_df, self.orders_df)
        pd.testing.assert_index_equal(pd.Index(result), pd.Index(expected_output_df))
