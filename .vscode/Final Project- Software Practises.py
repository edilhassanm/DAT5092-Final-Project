import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


# Assigning the file paths to their variables
earnings = r"C:\Users\edilh\OneDrive\earnings1.xlsx"
insecureWork = r"C:\Users\edilh\OneDrive\InsecureWork.xlsx"

## Error Handling
try:
    # Read Excel files into Pandas DataFrames
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

# This next section merges the two data frames and plots the data
   


# Plotting the time series
plt.figure(figsize=(10, 5))
plt.plot(df_insecure_work.columns[1:], df_insecure_work.iloc[0, 1:], label='Insecure Employment Numbers', marker='x', color='red')
plt.plot(df_earnings.columns[1:], df_earnings.iloc[0, 1:], label='Earning below LLW', marker='x', color= 'blue')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Number of People')
plt.title('Rates of Insecure Employment Compared to Rates of Earning below London Living Wage(LLW)')
plt.legend()
plt.grid(True)
plt.show()
