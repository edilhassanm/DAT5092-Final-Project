
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

# Assigning the file paths to their variables
earnings = r"C:\Users\edilh\OneDrive\earnings1.xlsx"
insecureWork = r"C:\Users\edilh\OneDrive\InsecureWork.xlsx"

## Error Handling
try:
    # Read Excel files into a Pandas DataFrames
    df_earnings = pd.read_excel(earnings)
    df_insecure_work = pd.read_excel(insecureWork)

    # Print the DataFrames to preview the data
    print("Earnings DataFrame:")
    print(df_earnings)

    

except FileNotFoundError:
    print("Error: One or more files not found. Please check the file paths.")
except pd.errors.EmptyDataError:
    print("Error: One or more files are empty.")
except pd.errors.ParserError:
    print("Error: Unable to parse Excel file. Please check the file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 


# Plotting the time series
plt.figure(figsize=(10, 6))
plt.plot(df_insecure_work.columns[1:], df_insecure_work.iloc[0, 1:], label='Insecure Employment Numbers', marker='x', color ='red')
plt.plot(df_earnings.columns[1:], df_earnings.iloc[0, 1:], label='Earning below LLW', marker='x', color= 'purple')

# Add a title and appropriate labels
plt.xlabel('Year')
plt.ylabel('Number of People')
plt.title('Figure 1. Rates of Insecure Employment Compared to Rates of Earning below London Living Wage(LLW)')
plt.legend()
plt.grid(True) # This line adds grid lines to the visualisation
plt.show()

# The following code plots the changes in the LLw between 2015 and 2023 

#Reading the data from the file
file_path = "C:\Users\edilh\OneDrive\full_earnings_data.xlsx"

data = pd.read_excel(file_path)

#Extracts the first row from the data
years = data.columns[1:]
london_living_wage = data.iloc[0, 1:].astype(float)

plt.plot(years, london_living_wage, marker='o',color= 'purple')
plt.title('Figure 2. Changes in the London Living Wage Over the Years')
plt.xlabel('Year')
plt.ylabel('London Living Wage (£)')
plt.grid(True)
plt.show()

