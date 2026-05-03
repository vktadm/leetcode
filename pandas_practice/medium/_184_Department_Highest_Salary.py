import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame,
    department: pd.DataFrame,
) -> pd.DataFrame:
    """Write a solution to find employees who have the highest salary in each of the departments"""
    dep_empl = pd.merge(
        department,
        employee,
        left_on="id",
        right_on="departmentId",
        how="inner",
    )
    filtered = dep_empl.groupby("departmentId")["salary"].transform("max")
    highest_salary = dep_empl.loc[filtered == dep_empl["salary"]]
    result = highest_salary[["name_x", "salary", "name_y"]].rename(
        columns={
            "name_y": "Department",
            "name_x": "Employee",
            "salary": "Salary",
        }
    )
    return result


if __name__ == "__main__":
    employee_data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
        "salary": [70000, 90000, 80000, 60000, 90000],
        "departmentId": [1, 1, 2, 2, 1],
    }
    employee_df = pd.DataFrame(employee_data)

    department_data = {"id": [1, 2], "name": ["IT", "Sales"]}
    department_df = pd.DataFrame(department_data)

    department_highest_salary(employee_df, department_df)
