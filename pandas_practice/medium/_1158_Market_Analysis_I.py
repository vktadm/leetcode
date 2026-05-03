import pandas as pd
from datetime import date


def market_analysis(
    users: pd.DataFrame,
    orders: pd.DataFrame,
    items: pd.DataFrame,
) -> pd.DataFrame:
    """Write a solution to find for each user, the join date and the number of orders they made as a buyer in 2019."""
    joined = users.merge(orders, left_on="user_id", right_on="buyer_id", how="left")
    grouped = (
        joined.groupby(["user_id", "join_date"])
        .agg(orders_in_2019=("order_date", lambda x: (x.dt.year == 2019).sum()))
        .reset_index()
    )
    result = grouped[["user_id", "join_date", "orders_in_2019"]].rename(
        columns={"user_id": "buyer_id"}
    )
    return result


if __name__ == "__main__":
    # Users table
    users_data = {
        "user_id": [1, 2, 3, 4, 5],
        "join_date": [
            "2018-01-01",
            "2018-02-09",
            "2018-01-19",
            "2018-05-21",
            "2018-08-21",
        ],
        "favorite_brand": ["Lenovo", "Samsung", "LG", "HP", "Samsung"],
    }
    users_df = pd.DataFrame(users_data)
    users_df["join_date"] = pd.to_datetime(users_df["join_date"])

    # Orders table
    orders_data = {
        "order_id": [1, 2, 3, 4, 5, 6],
        "order_date": [
            "2019-08-01",
            "2018-08-02",
            "2019-08-03",
            "2018-08-04",
            "2018-08-04",
            "2019-08-05",
        ],
        "item_id": [4, 2, 3, 1, 1, 2],
        "buyer_id": [1, 1, 2, 4, 3, 2],
        "seller_id": [2, 3, 3, 2, 4, 4],
    }
    orders_df = pd.DataFrame(orders_data)
    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])

    # Items table
    items_data = {
        "item_id": [1, 2, 3, 4],
        "item_brand": ["Samsung", "Lenovo", "LG", "HP"],
    }
    items_df = pd.DataFrame(items_data)
    market_analysis(users_df, orders_df, items_df)
