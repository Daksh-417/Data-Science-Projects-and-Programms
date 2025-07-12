import pandas as pd

# Define the dataset
data = {
    'Student': ['Amit', 'Riya', 'Sohan', 'Neha', 'Rahul', 'Anjali', 'Ravi', 'Priya', 'Rohan', 'Meena'],
    'Maths': [78, 56, 90, 45, 66, 56, 90, 66, 78, 45],
    'Science': [85, 59, 91, 52, 72, 60, 88, 65, 80, 48],
    'English': [67, 61, 89, 50, 70, 65, 91, 67, 79, 51],
    'SST': [74, 65, 93, 49, 68, 62, 90, 66, 76, 47]
}

df = pd.DataFrame(data)

# Save to csv
df.to_csv('student_scores.csv', index=False)
print("csv file created successfully!")
