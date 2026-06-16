import unittest
import pandas as pd


def bigCountries(world: pd.DataFrame) -> pd.DataFrame:
    world = world.loc[(world["area"] >= 3000000) | (world["population"] >= 25000000)]
    world = world.reset_index()
    return world[["name", "population", "area"]]


class TestBigCountries(unittest.TestCase):
    def test_example_1(self):
        data = {
            "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
            "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
            "area": [652230, 28748, 2381741, 468, 1246700],
            "population": [25500100, 2831741, 37100000, 78115, 20609294],
            "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000],
        }
        world = pd.DataFrame(data)

        result = bigCountries(world)

        expected_data = {
            "name": ["Afghanistan", "Algeria"],
            "population": [25500100, 37100000],
            "area": [652230, 2381741],
        }
        expected = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(
            result.reset_index(drop=True),
            expected.reset_index(drop=True),
            check_dtype=False,
        )

    def test_no_big_countries(self):
        data = {
            "name": ["Small1", "Small2"],
            "continent": ["Asia", "Europe"],
            "area": [100000, 500000],
            "population": [1000000, 5000000],
            "gdp": [1000000000, 2000000000],
        }
        world = pd.DataFrame(data)

        result = bigCountries(world)
        self.assertTrue(result.empty)

    def test_all_big_countries(self):
        data = {
            "name": ["Big1", "Big2"],
            "continent": ["Asia", "Africa"],
            "area": [4000000, 1000000],
            "population": [10000000, 30000000],
            "gdp": [50000000000, 60000000000],
        }
        world = pd.DataFrame(data)

        result = bigCountries(world)
        self.assertEqual(len(result), 2)

    def test_boundary_conditions(self):
        data = {
            "name": ["ExactArea", "ExactPop", "Both"],
            "continent": ["Asia", "Europe", "Africa"],
            "area": [3000000, 1000000, 3000000],
            "population": [10000000, 25000000, 25000000],
            "gdp": [10000000000, 20000000000, 30000000000],
        }
        world = pd.DataFrame(data)

        result = bigCountries(world)
        self.assertEqual(len(result), 3)

    def test_empty_dataframe(self):
        world = pd.DataFrame(columns=["name", "continent", "area", "population", "gdp"])
        result = bigCountries(world)
        self.assertTrue(result.empty)

    def test_large_numbers(self):
        data = {
            "name": ["China", "India", "Monaco"],
            "continent": ["Asia", "Asia", "Europe"],
            "area": [9706961, 3287590, 2],
            "population": [1439323776, 1380004385, 39244],
            "gdp": [17700000000000, 3000000000000, 7000000000],
        }
        world = pd.DataFrame(data)

        result = bigCountries(world)
        self.assertEqual(len(result), 2)
        self.assertIn("China", result["name"].values)
        self.assertIn("India", result["name"].values)


if __name__ == "__main__":
    unittest.main()
