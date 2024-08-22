def sales_management(member_names, member_records):
    average_records = [sum(records) / len(records) for records in member_records]
    
    top_performers = sorted(range(len(average_records)), key=lambda i: average_records[i], reverse=True)[:2]
    
    worst_performers = sorted(range(len(average_records)), key=lambda i: average_records[i])[:2]
    
    bonus_recipients = []
    interview_candidates = []
    
    for i in range(len(member_names)):
        if i in top_performers and average_records[i] > 5:
            bonus_recipients.append(member_names[i])
        if i in worst_performers and average_records[i] <= 3:
            interview_candidates.append(member_names[i])

    print("보너스 대상자", ", ".join(bonus_recipients))
    print("면담 대상자", ", ".join(interview_candidates))

member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [
    [4,5,3,5,6,5,3,4,1,3,4,5],
    [2,3,4,3,1,2,0,3,2,5,7,2],
    [1,3,0,3,3,4,5,6,7,2,2,1],
    [3,2,9,2,3,5,6,6,4,6,9,9],
    [8,7,7,5,6,7,5,8,8,6,10,9],
    [7,8,4,9,5,10,3,3,2,2,1,3]
]
sales_management(member_names, member_records)
