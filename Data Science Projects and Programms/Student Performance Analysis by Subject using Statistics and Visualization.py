import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🧮 1. Read the Dataset
df = pd.read_csv('student_scores.csv')

# 🔍 2. Data Cleaning
print("Missing values:\n", df.isnull().sum())
# Validate marks range (0–100)
if not df.iloc[:, 1:].applymap(lambda x: 0 <= x <= 100).all().all():
    print("⚠️ Warning: Some values are outside 0–100 range.")

# 📊 3. Descriptive Statistics for Each Subject
stats = df.describe(include='all')
print("\nDescriptive Statistics:\n", stats)
# Mean, Median, Mode, Std Dev, Variance
for subject in df.columns[1:]:
    print(f"\n📘 Stats for {subject}:")
    print("Mean:", df[subject].mean())
    print("Median:", df[subject].median())
    print("Mode:", df[subject].mode()[0])
    print("Standard Deviation:", df[subject].std())
    print("Variance:", df[subject].var())
# 🔝 Identify most and least scoring subjects (by average)
subject_means = df.iloc[:, 1:].mean()
print("\n🎯 Highest Scoring Subject:", subject_means.idxmax())
print("🔻 Lowest Scoring Subject:", subject_means.idxmin())

# 🧑‍🎓 4. Student-Wise Analysis
df['Total'] = df.iloc[:, 1:].sum(axis=1)
df['Average'] = df.iloc[:, 1:].mean(axis=1)
def get_category(avg):
    if avg >= 85: return 'Excellent'
    elif avg >= 70: return 'Good'
    elif avg >= 50: return 'Average'
    else: return 'Needs Improvement'
df['Category'] = df['Average'].apply(get_category)
print("\n🧑‍💻 Student Performance:\n", df[['Student', 'Total', 'Average', 'Category']])

# 🏆 5. Subject-Wise Toppers
print("\n🏅 Subject Toppers:")
for subject in df.columns[1:5]:
    topper = df[df[subject] == df[subject].max()]
    name = topper['Student'].values[0]
    score = topper[subject].values[0]
    print(f"{subject}: {name} ({score})")

# 📊 6. Visualizations
# Bar Chart – Total Marks
plt.figure(figsize=(8,5))
sns.barplot(x='Student', y='Total', data=df, palette='viridis')
plt.title('Total Marks per Student')
plt.xticks(rotation=45)
plt.show()
# Line Chart – Subject-Wise Average
plt.figure(figsize=(8,5))
subject_means.plot(kind='line', marker='o', color='darkgreen')
plt.title('Average Marks by Subject')
plt.ylabel('Average Marks')
plt.grid(True)
plt.show()
# Boxplot – Subject Spread
plt.figure(figsize=(10,6))
sns.boxplot(data=df.iloc[:, 1:5], palette='pastel')
plt.title('Marks Spread per Subject')
plt.show()
# Histogram – Distribution per Subject
plt.figure(figsize=(10,6))
for subject in df.columns[1:5]:
    sns.histplot(df[subject], bins=5, kde=True, label=subject)
plt.title('Marks Distribution Across Subjects')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.legend()
plt.show()