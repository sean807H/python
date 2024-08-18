def calculate_score(student_answer, correct_answer):
    score = 0
    for s_answer, c_answer in zip(student_answer, correct_answer):
        if s_answer == c_answer:
            score += 1
    return score

def grader(s, a):
    student_scores = []
    
    for student_info in s:
        name, answer = student_info.split(',')
        score = calculate_score(answer, a)
        student_scores.append((name, score))
    
    student_scores.sort(key=lambda x: (x[1], x[0]), reverse=True)
    
    print("학생 점수와 등수:")
    for idx, (name, score) in enumerate(student_scores, start=1):
        rank = "등" if idx > 1 and student_scores[idx - 1][1] == score else "등 1"
        print(f"학생: {name} 점수: {score}점 {idx}{rank}")

if __name__ == "__main__":
    s = [
        "김갑,3242524215",
        "이을,3252524215",
        "박병,3242524225",
        "최정,3242524235",
        "정무,3242524215",
        "진기,3242524215",
        "이신,3342524215",
        "강신,3242524215",
        "한갈,3242524215",
        "이갈,3242524215"
    ]
    
    a = "3242524215"  # 정답
    
    grader(s, a)
