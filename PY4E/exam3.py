def bus(age, pay):
    if age < 8:
        return 0
    elif 8 <= age < 14:
        if pay == "카드":
            return 450
        else:
            return 450
    elif 14 <= age < 20:
        if pay == "카드":
            return 720
        else:
            return 1000
    elif 20 <= age < 75:
        if pay == "카드":
            return 1200
        else:
            return 1300
    else:
        return 0

def bus_fare(age, pay):
    fare = bus(age, pay)
    if fare == 0:
        return "무료입니다."
    else:
        return fare

def main():
    age = 30
    pay = "현금"

    bus = bus_fare(age, pay)
    print(f"나이: {age}세")
    print(f"지불 유형: {pay}")
    print(f"버스 요금: {bus}원")

if __name__ == "__main__":
    main()
    
