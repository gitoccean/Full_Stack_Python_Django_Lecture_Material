def grade():
    if 90 <= marks <= 100:
         return 'A'
    elif 80 <= marks < 90:
         return  'B'
    elif 70 <= marks < 80:
         return  'C'
    elif 60 <= marks < 70:
         return  'D'
    elif marks > 100:
        return "Invalid Grade Ranking."
    else:
         return  'F'

def feedback():
    if grade == 'A':
        return 'Excellent work!'
    elif grade == 'B':
        return 'Good Job!'
    elif grade == 'C':
        return 'Fair effort!'
    elif grade == 'D':
        return 'You are Pass!'
    elif grade == "Invalid Grade Ranking.":
        return 'Marks should be between 0 and 100.'
    else:
        return 'You are Fail! better luck next time!'


marks = int(input('Enter your marks in numbers: '))
grade=grade()

feedback=feedback()


print(f'Your grade is {grade}')
print(f'Feedback: {feedback}')
