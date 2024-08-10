def find_even_number(n, m):
    
    start = min(n, m)
    end = max(n, m)

    # 짝수만 출력하고 중앙값 계산
    numbers = []
    median = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            numbers.append(num)

    if len(numbers) > 0:
        median_index = len(numbers) // 2
        median = numbers[median_index]

    # 결과
    for num in numbers:
        print(f"{num} 짝수")
    if median != 0:
        print(f"{median} 중앙값")
    else:
        print("중앙값이 없습니다.")

# 두 개의 숫자 입력 받기
try:
    num1 = int(input("첫 번째 수 입력 : "))
    num2 = int(input("두 번째 수 입력 : "))

    find_even_number(num1, num2)

except ValueError:
    print("알맞은 숫자를 입력하세요.")
