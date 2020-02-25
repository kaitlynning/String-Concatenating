score = float(input('grade: '))
if score >= 90:
    grade = 'A Excellent'
elif score >= 80:
    grade = 'B Good'
elif score >= 70:
    grade = 'C Fair'
elif score >= 60:
    grade = 'D needs improvement'
else:
    grade = 'E poor'
    
print('score:', grade)

'''
grade: 90
score: A Excellent
'''