# 📊 Student Performance Analysis

**Project 01 — Data Cleaning, EDA & Visualization**

A complete, beginner-level walkthrough of the standard data analysis pipeline — load → clean → describe → compare → visualize → conclude — applied to a public dataset of 1,000 students' exam scores. The goal wasn't to produce as many charts as possible; it was to notice something real in the data and explain it clearly. Every chart and table here is followed by a plain-language interpretation of what it actually shows.

---

## 📁 Dataset

**Name:** Students Performance in Exams
**Source:** [Kaggle — spscientist/students-performance-in-exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) (originally shared by Royce Kimmons)
**Local copy:** [`StudentsPerformance.csv`](StudentsPerformance.csv)
**Size:** 1,000 rows × 8 columns

| Column | Type | Description |
|---|---|---|
| `gender` | categorical | female / male |
| `race/ethnicity` | categorical | anonymized group A–E |
| `parental level of education` | categorical | highest education level of the student's parent(s) |
| `lunch` | categorical | standard / free-reduced — a common socio-economic proxy in this dataset |
| `test preparation course` | categorical | none / completed |
| `math score` | numeric (0–100) | exam score |
| `reading score` | numeric (0–100) | exam score |
| `writing score` | numeric (0–100) | exam score |

---

## 🎯 Objective

This project builds the core foundation of any data role:

- Loading and inspecting raw data
- Discovering (and honestly reporting) what's wrong with it — or isn't
- Descriptive statistics and group comparisons
- Communicating findings through charts *with* interpretation, not charts alone
- Checking correlation between variables
- Summarizing findings in plain language

---

## 🛠️ Approach

1. **Load the data** — shape, columns, dtypes.
2. **Data quality check** — missing values, duplicate rows, out-of-range scores (should be 0–100), and inconsistent category labels.
3. **Descriptive statistics** — mean, median, mode, standard deviation, min, max for every numeric column.
4. **Group comparisons** — subject-wise, gender-wise, by test-prep completion, by lunch type, by parental education.
5. **Visualization** — bar chart, pie chart, histogram, box plot, and scatter plot, each with a written insight.
6. **Correlation check** — Pearson correlation between the three subject scores, shown as a table and a heatmap.
7. **Conclusion** — top 5 findings stated in plain language.

---

## 🔍 Data Quality — What Was Found

✅ **Zero missing values**
✅ **Zero duplicate rows**
✅ **Zero out-of-range scores** (all within 0–100)
✅ **Consistent category labels** — no typos, no stray casing/whitespace

The dataset needed no cleaning. This is reported as an explicit finding rather than skipped, since confirming a dataset is *actually* clean is part of a real quality check, not something to assume. The only preparation step taken was adding a derived `average score` column (mean of math, reading, writing) to simplify group comparisons.


---

## 🧰 Tools & Libraries

- Python 3
- pandas, NumPy
- matplotlib, seaborn
- SciPy
- VS Code

---

## 👤 Author

**Mohammad Aman Malik**
M.Sc. Operational Research, University of Delhi
