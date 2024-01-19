import unittest
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

class TestFinalProject(unittest.TestCase):
    def test_file_existence(self):
        self.assertTrue(os.path.isfile(r"C:\Users\edilh\OneDrive\earnings1.xlsx"))
        self.assertTrue(os.path.isfile(r"C:\Users\edilh\OneDrive\InsecureWork.xlsx"))
        self.assertTrue(os.path.isfile(r"C:\Users\edilh\OneDrive\full_earnings_data.xlsx"))

    def test_read_excel_files(self):
        df_earnings = pd.read_excel(r"C:\Users\edilh\OneDrive\earnings1.xlsx")
        df_insecure_work = pd.read_excel(r"C:\Users\edilh\OneDrive\InsecureWork.xlsx")
        self.assertIsInstance(df_earnings, pd.DataFrame)
        self.assertIsInstance(df_insecure_work, pd.DataFrame)
        
def test_plotting(self):
    # Test plotting Figure 1
    plt.figure(figsize=(10, 6))
    with self.assertRaises(IndexError):
        plt.plot([], [])
        plt.xlabel('Year')  # Adding this line to create an IndexError
    plt.close()

    # Test plotting Figure 2
    file_path = r"C:\Users\edilh\OneDrive\full_earnings_data.xlsx"
    data = pd.read_excel(file_path)
    years = data.columns[1:]
    london_living_wage = data.iloc[0, 1:].astype(float)
    plt.plot(years, london_living_wage, marker='o', color='purple')
    plt.close()

    # Test plotting Figure 3
    file_path = r"C:\Users\edilh\OneDrive\full_earnings_data.xlsx"
    df = pd.read_excel(file_path)
    plt.figure(figsize=(12, 8))
    with self.assertRaises(KeyError):
        sns.pointplot(data=df[:36], x='NonexistentColumn', y=2022, color='purple', markers='o', label='2022')
    plt.close()

    def test_data_frame_columns(self):
        # Test if the expected columns exist in the DataFrame
        file_path = r"C:\Users\edilh\OneDrive\full_earnings_data.xlsx"
        df = pd.read_excel(file_path)
        expected_columns = ['Area name', 2022]  # Update with the actual expected columns
        for col in expected_columns:
            self.assertIn(col, df.columns)

if __name__ == '__main__':
    unittest.main()
