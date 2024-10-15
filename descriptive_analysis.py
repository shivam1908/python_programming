# Import necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
file_path = 'P:\\python_programming\\python_programming\\data\\descriptive_sample_data.csv'
df = pd.read_csv(file_path)

# Display the first 5 and last 4 rows of the dataset
print("Top 5 Rows:")
print(df.head(5))

print("\nBottom 4 Rows:")
print(df.tail(4))

# Filter data for patients with AnxtyLH = 1
anxtyLH_1 = df[df['AnxtyLH'] == 1]
print("\nPatients with AnxtyLH = 1:")
print(anxtyLH_1)

# Calculate the average age for patients with AnxtyLH = 0
average_age_anxtyLH_0 = df[df['AnxtyLH'] == 0]['Age'].mean()
print("\nAverage Age for Patients with AnxtyLH = 0:", average_age_anxtyLH_0)

# Mean, Median, Skewness, and Kurtosis for Age, BP, and Chlstrl
mean_values = df[['Age', 'BP', 'Chlstrl']].mean()
median_values = df[['Age', 'BP', 'Chlstrl']].median()
skewness_values = df[['Age', 'BP', 'Chlstrl']].skew()
kurtosis_values = df[['Age', 'BP', 'Chlstrl']].kurt()

print("\nMean Values for Age, BP, and Chlstrl:")
print(mean_values)

print("\nMedian Values for Age, BP, and Chlstrl:")
print(median_values)

print("\nSkewness for Age, BP, and Chlstrl:")
print(skewness_values)

print("\nKurtosis for Age, BP, and Chlstrl:")
print(kurtosis_values)

# Max and Min values for Age, BP, and Chlstrl
max_values = df[['Age', 'BP', 'Chlstrl']].max()
min_values = df[['Age', 'BP', 'Chlstrl']].min()

print("\nMaximum Values for Age, BP, and Chlstrl:")
print(max_values)

print("\nMinimum Values for Age, BP, and Chlstrl:")
print(min_values)

# Correlation between different columns
correlation = df.corr()
print("\nCorrelation Matrix:")
print(correlation)

# End of script
