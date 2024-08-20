def get_date_and_day():
    while True:
        try:
            date_input = input("날짜를 입력하세요 (MM/DD): ")
            month, day = map(int, date_input.split('/'))
            if not (1 <= month <= 12 and 1 <= day <= 31):
                print("올바른 날짜 형식이 아닙니다. 다시 입력하세요.")
                continue
            day_input = input("요일을 입력하세요 (월~일): ")
            days_of_week = ["월", "화", "수", "목", "금", "토", "일"]
            day_index = days_of_week.index(day_input)
            return month, day, day_index
        except ValueError:
            print("올바른 형식으로 입력하세요.")

def calculate_date(month, day, days_to_add):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    new_day = day + days_to_add
    new_month = month
    while new_day > month_days[new_month]:
        new_day -= month_days[new_month]
        new_month += 1
        if new_month > 12:
            new_month = 1
    return new_month, new_day

def calculate_day(day_index, days_to_add):
    days_of_week = ["월", "화", "수", "목", "금", "토", "일"]
    new_day_index = (day_index + days_to_add) % 7
    return days_of_week[new_day_index]

def main():
    print("날짜 계산기")
    print("100일 후의 날짜와 요일을 계산합니다.")

    month, day, day_index = get_date_and_day()
    new_month, new_day = calculate_date(month, day, 100)
    new_day_of_week = calculate_day(day_index, 100)

    print(f"입력한 날짜: {month}월 {day}일 ({calculate_day(day_index, 0)})")
    print(f"100일 후의 날짜: {new_month}월 {new_day}일 ({new_day_of_week})")

if __name__ == "__main__":
    main()
