student_scores = [12, 32, 32, 24, 2, 4, 4, 3, 4546, 65, 768, 68, 797, 9, 4534, 34, 2, 32, 3, 23]
# total_exam_score = sum(student_scores)
# print(total_exam_score)
#
# Tsum = 0
# for score in student_scores:
#     Tsum = Tsum + score
#
# print(Tsum)




# print(max(student_scores))


maxScore=0
for score in student_scores:
    if score>maxScore:
        maxScore=score

print(maxScore)




