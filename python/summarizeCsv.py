import pandas as pd
import sys

def summarize_csv(file_path):
    """
    Loads a CSV file and prints a summary including head, info, and descriptive statistics.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Print first few rows
        print("First 5 rows of the CSV:")
        print(df.head())
        print("\n")
        
        # Print DataFrame info (columns, types, non-null counts)
        print("DataFrame Info:")
        df.info()
        print("\n")
        
        # Print descriptive statistics (for numerical columns)
        print("Descriptive Statistics:")
        print(df.describe())
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    summarize_csv(file_path)