#This program is to find the  maximum number without using inbuilt max function

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
highest = student_scores[0]
for number in student_scores:
    if number> highest:
        highest=number

print(highest)
