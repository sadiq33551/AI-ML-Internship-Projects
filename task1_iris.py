# Task 1: Exploring and Visualizing Iris Dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("iris")

# Basic Information
print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())

print(df.info())
print(df.describe())

# Scatter Plot
plt.figure()
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.title("Sepal Length vs Petal Length")
plt.show()

# Histogram
plt.figure()
df.hist()
plt.show()

# Box Plot
plt.figure()
sns.boxplot(data=df)
plt.title("Boxplot of Iris Features")
plt.show()