import os

print("Current Folder:", os.getcwd())
print("Files:", os.listdir())
import pandas as pd

# Load Dataset
df = pd.read_csv("students.csv")

print("===== ORIGINAL DATA =====")
print(df)

# Inspect Dataset
print("\n===== DATA INFO =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Clean Missing Data
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\n===== CLEANED DATA =====")
print(df)

# Filtering
print("\n===== STUDENTS WITH MARKS > 80 =====")
high_marks = df[df["Marks"] > 80]
print(high_marks)

# Grouping and Aggregation
print("\n===== AVERAGE MARKS BY DEPARTMENT =====")
dept_avg = df.groupby("Department")["Marks"].mean()
print(dept_avg)

print("\n===== MAX MARKS BY DEPARTMENT =====")
dept_max = df.groupby("Department")["Marks"].max()
print(dept_max)

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())
