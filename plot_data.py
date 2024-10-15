# Import necessary libraries for data visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'P:\\python_programming\\python_programming\\data\\descriptive_sample_data.csv'
data = pd.read_csv(file_path)



# 1. Create a Histogram for Age, BP, and Chlstrl data
def plot_histograms(data):
    plt.figure(figsize=(15, 5))

    # Histogram for Age
    plt.subplot(1, 3, 1)
    plt.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Histogram of Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    # Histogram for Blood Pressure (BP)
    plt.subplot(1, 3, 2)
    plt.hist(data['BP'], bins=10, color='lightgreen', edgecolor='black')
    plt.title('Histogram of Blood Pressure (BP)')
    plt.xlabel('BP')
    plt.ylabel('Frequency')

    # Histogram for Cholesterol (Chlstrl)
    plt.subplot(1, 3, 3)
    plt.hist(data['Chlstrl'], bins=10, color='lightcoral', edgecolor='black')
    plt.title('Histogram of Cholesterol (Chlstrl)')
    plt.xlabel('Cholesterol Level')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

# 2. Create Scatter Plot for Age vs DrugR1
def scatter_plot_age_vs_drugR1(data):
    plt.figure(figsize=(7, 5))
    plt.scatter(data['Age'], data['DrugR1'], color='blue')
    plt.title('Scatter Plot: Age vs DrugR1')
    plt.xlabel('Age')
    plt.ylabel('Drug Response (DrugR1)')
    plt.grid(True)
    plt.show()

# 3. Create Scatter Plot for BP vs DrugR1
def scatter_plot_bp_vs_drugR1(data):
    plt.figure(figsize=(7, 5))
    plt.scatter(data['BP'], data['DrugR1'], color='green')
    plt.title('Scatter Plot: BP vs DrugR1')
    plt.xlabel('Blood Pressure (BP)')
    plt.ylabel('Drug Response (DrugR1)')
    plt.grid(True)
    plt.show()

# 4. Create Scatter Plot for Chlstrl vs DrugR1
def scatter_plot_chlstrl_vs_drugR1(data):
    plt.figure(figsize=(7, 5))
    plt.scatter(data['Chlstrl'], data['DrugR1'], color='red')
    plt.title('Scatter Plot: Cholesterol vs DrugR1')
    plt.xlabel('Cholesterol Level')
    plt.ylabel('Drug Response (DrugR1)')
    plt.grid(True)
    plt.show()

# 5. Create a Pie Chart for AnxtyLH (Anxiety Levels)
def pie_chart_anxtylh(data):
    plt.figure(figsize=(5, 5))
    anxiety_counts = data['AnxtyLH'].value_counts()
    plt.pie(anxiety_counts, labels=['No Anxiety', 'Anxiety'], autopct='%1.1f%%', colors=['lightblue', 'salmon'])
    plt.title('Pie Chart: Anxiety Levels (AnxtyLH)')
    plt.show()

# 6. Create a Box Plot for Age
def box_plot_age(data):
    plt.figure(figsize=(5, 7))
    sns.boxplot(y=data['Age'], color='lightblue')
    plt.title('Box Plot of Age')
    plt.ylabel('Age')
    plt.show()

# 7. Create a Violin Plot for BP and Chlstrl
def violin_plot_bp_chlstrl(data):
    plt.figure(figsize=(10, 6))

    # Violin plot for Blood Pressure (BP)
    plt.subplot(1, 2, 1)
    sns.violinplot(y=data['BP'], color='lightgreen')
    plt.title('Violin Plot of Blood Pressure (BP)')
    plt.ylabel('BP')

    # Violin plot for Cholesterol (Chlstrl)
    plt.subplot(1, 2, 2)
    sns.violinplot(y=data['Chlstrl'], color='lightcoral')
    plt.title('Violin Plot of Cholesterol (Chlstrl)')
    plt.ylabel('Cholesterol')

    plt.tight_layout()
    plt.show()

# Run all the plots
plot_histograms(data)
scatter_plot_age_vs_drugR1(data)
scatter_plot_bp_vs_drugR1(data)
scatter_plot_chlstrl_vs_drugR1(data)
pie_chart_anxtylh(data)
box_plot_age(data)
violin_plot_bp_chlstrl(data)
