import pandas as pd
import numpy as np

def reformat_dataframe_to_3d(df, operator_column, part_column, measurement_column):
    # Get unique operators and parts, and sort them to ensure consistent ordering
    operators = sorted(df[operator_column].unique())
    parts = sorted(df[part_column].unique())
    
    # Create a 3D numpy array filled with NaN values
    max_measurements = df.groupby([operator_column, part_column])[measurement_column].count().max()
    result = np.full((len(operators), len(parts), max_measurements), np.nan)
    
    # Iterate through the DataFrame and fill the 3D array
    for (operator, part), group in df.groupby([operator_column, part_column]):
        i = operators.index(operator)
        j = parts.index(part)
        measurements = group[measurement_column].values
        result[i, j, :len(measurements)] = measurements
    
    return result

# Example usage:
# Assuming 'df' is your pandas DataFrame
# result = reformat_dataframe_to_3d(df, 'operator_column', 'part_column', 'measurement_column')
# print(result)

if __name__ == '__main__':
# Demonstrate the code functioning

    # Create a sample DataFrame
    data = {
        'operator': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'part': ['X', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'X', 'X', 'Y'],
        'measurement': [1.1, 1.2, 2.1, 2.2, 3.1, 4.1, 4.2, 5.1, 5.2, 6.1]
    }

    df = pd.DataFrame(data)
    print("Sample DataFrame:")
    print(df)
    print()

    # Apply the function
    result = reformat_dataframe_to_3d(df, 'operator', 'part', 'measurement')

    print("Resulting 3D Array:")
    print(result)
    print()

    print("Array shape:", result.shape)
    print()

    print("Detailed view of the 3D array:")
    for i, operator in enumerate(['A', 'B', 'C']):
        for j, part in enumerate(['X', 'Y']):
            print(f"Operator {operator}, Part {part}:")
            print(result[i, j])
        print()