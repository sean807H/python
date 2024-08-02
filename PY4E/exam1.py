def x(score):
    if score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "C+"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D+"
    elif score >= 60:
        return "D"
    else:
        return "F"

def grader(name, score):
    grade = x(score)
    print(f"학생 이름: {name}")
    print(f"점수: {score}")
    print(f"학점: {grade}")

#실행 예시
grader("이호창", 99)
