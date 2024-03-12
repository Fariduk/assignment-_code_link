
import pandas as pd

# Define the file path
parquet_file = r'C:\Users\AUTOMATION\Desktop\plm.parquet'

# Read the Parquet file into a DataFrame
df = pd.read_parquet(parquet_file)

# Now you can work with the DataFrame 'df'
print(df.head())  # Display the first few rows of the DataFrame

