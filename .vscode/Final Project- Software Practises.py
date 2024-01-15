import pandas as pd
import matplotlib.pyplot as plt

# Replace 'path/to/your_file.xlsx' with the correct path to your Excel file
excel_file_path = 'smoking-quitters.xlsx'

try:
    # Read Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

    # Plot a simple graph using matplotlib (customize based on your data)
    plt.plot(df['Column1'], df['Column2'])
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Your Plot Title')
    plt.show()

except pd.errors.EmptyDataError:
    print("The Excel file is empty or contains no data.")

except FileNotFoundError:
    print(f"File not found at the specified path: {excel_file_path}")

except Exception as e:
    print("An error occurred: {}".format(e))

