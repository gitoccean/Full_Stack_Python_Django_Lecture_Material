import pandas as pd

# Sample student data
data = {
    'Student ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math Score': [85, 90, 78, 92, 88],
    'English Score': [92, 88, 76, 95, 89],
    'Comments': ['Good work. Needs improvement in math.', 'Excellent student.', 'Work hard in English.',
                 'Top performer!', 'Well done.'],
}
data_frame = pd.DataFrame(data)


def calculate_grade():
    data_frame.insert(4, 'Grade', 5)
    data_frame['Percentage'] = ((data_frame['Math Score'] + data_frame['English Score']) / 200) * 100

    data_frame.loc[data_frame['Percentage'] >= 90, 'Grade'] = 'A'
    data_frame.loc[(data_frame['Percentage'] >= 80) & (data_frame['Percentage'] < 90), 'Grade'] = 'B'
    data_frame.loc[(data_frame['Percentage'] >= 70) & (data_frame['Percentage'] < 80), 'Grade'] = 'C'
    data_frame['Grade'] = 'D'
    data_frame.pop('Percentage')


while True:
    print("Menu:")
    print("1. Calculate Grades")
    print("2. Count Words in Comments")
    print("3. Display Specific Student Information")
    print("4. Exit")
    choice = int(input("Enter your choice:  "))

    if choice == 1:
        calculate_grade()
        print("Grades calculated and updated.")
        print(data_frame)

    elif choice == 2:
        def count_words(comment):
            return len(comment.replace(" ",''))


        data_frame['Word Count'] = data_frame['Comments'].apply(count_words)

        print("Comments\'s Words count ")
        print(data_frame)
    elif choice == 3:
        name = input("Enter The Student\'s Name:  ")
        if name in data_frame['Name'].values:
            student_data = data_frame[data_frame['Name'] == name]
            print("Student Information for", name)
            print(student_data)
        else:
            print('Sorry! Student does not exist.')
    elif choice == 4:
        print("Thanks to visit Menu for Intellectual Student Information.")
        break
    else:
        print("Invalid your choice! Kindly look at Menu.")
