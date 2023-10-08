import pandas as pd

data = {
    'Student ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math Score': [85, 90, 78, 92, 88],
    'English Score': [92, 88, 76, 95, 89],
    'Comments': ['Good work. Needs improvement in math.', 'Excellent student.', 'Work hard in English.',
                 'Top performer!', 'Well done.'],
}

df = pd.DataFrame(data)


def calculate_grade(math_score, english_score):
    average_score = (math_score + english_score) / 2
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    else:
        return 'D'


def calculate_row_grade(row):
    math_score = row['Math Score']
    english_score = row['English Score']
    average_score = (math_score + english_score) / 2
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'


df['Grade'] = df.apply(calculate_row_grade, axis=1)


def word_count(comment):
    return len(comment.replace(" ",""))


df['Word Count'] = df['Comments'].apply(word_count)

specific_student = df[df['Student ID'] == 3]

print("Student Data:")
print(df)
print("\nSpecific Student Information:")
print(specific_student)
