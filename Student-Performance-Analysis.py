# Project 1: EDA 
# Student Performance Analyis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. load the dataset
url = "StudentsPerformance.csv"
df = pd.read_csv(url)

# 2. Understand the dataset
print("First 5 rows: ")
print(df.head())

print('\nDataset Shape :', df.shape )
print("\nColumn names : ")
print(df.columns.tolist())

print("\nDataset Information : ")
df.info()

# 3. Check the data quality
print("\nMissing values : ")
print(df.isnull().sum())

print("\nDuplicate Values : ",df.duplicated().sum())

print("\nStatistical Summary : ")
print(df.describe())


# 4. clean column name for easier coding 
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace('/', '_', regex=False)
    .str.replace(' ', '_', regex=False)
)


# 5. Create a total and average score
score_cols= ["math_score", "reading_score", "writing_score"]
df["total_score"]= df[score_cols].sum(axis=1)
df["average_score"]= df[score_cols].mean(axis=1)


# 6. Distribution of total score
df[score_cols].hist(bins=20, figsize=(12,4), edgecolor='black')
plt.suptitle("Distribution of Total score")
plt.tight_layout()
plt.show()

# 7. correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(
    df[score_cols + ["total_score"]].corr(),
    annot=True,
    cmap="coolwarm", #coolwarm_r is for reversed color map
    fmt=".2f",
    vmin=-1,
    vmax=1,
    center=0
)
plt.title("Correlation between exam scores")
plt.show()


# 8. Average score by gender
gender_scores = df.groupby("gender")[score_cols].mean()
print("\nAverage score by gender : ")
print(gender_scores.round(2))

gender_scores.plot(kind="bar", figsize=(10,5))
plt.title("Average score by gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 9.Test preparation analysis
prep_scores=df.groupby("test_preparation_course")[score_cols].mean()
print("\nAverage score by test preparation Course : ")
print(prep_scores.round(2))

prep_scores.plot(kind="bar", figsize=(10,5))
plt.title("Test preparation vs Average score")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 10. Lunch type and performance
lunch_scores = df.groupby("lunch")[score_cols].mean()
print("\n Average scores by lunch type : ")
print(lunch_scores.round(2))

lunch_scores.plot(kind='bar', figsize=(10,5))
plt.title("Average score by Lunch type")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# 11. Parental education and performance
parent_scores = df.groupby("parental_level_of_education")[score_cols].mean()
print("\nScores by parental education:")
print(parent_scores.round(2))

parent_scores.plot(kind="bar", figsize=(11, 5))
plt.title("Parental Education vs Student Scores")
plt.ylabel("Average score")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.show()


# 12. Relationship between reading and writing
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, x="reading_score", y="writing_score",
    hue="gender", alpha=0.7
)
plt.title("Reading Score vs Writing Score")
plt.tight_layout()
plt.show()


# 13. Outlier analysis using boxplots
plt.figure(figsize=(10, 5))
sns.boxplot(data=df[score_cols], orient='h')
plt.title("Outlier Analysis of Exam Scores")
plt.tight_layout()
plt.show()

# 14. Top 10 students by total score
print("\nTop 10 records by total score:")
print(
    df.nlargest(10, "total_score")[
        ["gender"] + score_cols + ["total_score"]
    ].to_string(index=False)
)

# 15. Final summary
print("\nOverall average scores:")
print(df[score_cols].mean().round(2))

print("\nOverall average score:", round(df["average_score"].mean(), 2))
print("Analysis completed successfully!")