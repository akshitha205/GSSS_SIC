
''' 
Accept the average score of the student 
'''
average_score = int(input("enter your score to print result :"))
if average_score < 0 or average_score >100:
    print("invalid score")
if average_score < 0 and average_score <= 59:
    print("result is failed")
elif average_score >= 60 and average_score <= 84:
    print("result is second class")
elif average_score >= 85 and average_score <= 95:
    print('result is pass')
else:
    print('result is excellent')
