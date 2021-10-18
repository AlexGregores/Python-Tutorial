# tuple = collection which is ordered and unchangeable
#         used to group together related data

student=('Alex', 21, 'male')
print (student.count('Alex') )
print(student.index('male'))

for x in student:
    print(x)
if 'Alex' in student:
    print('Alex is here')
