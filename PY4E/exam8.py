def is_prime(num):
    # 소수인지 여부를 확인하는 함수
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_number(n, m):
    # 입력된 두 숫자 중 작은 값과 큰 값 확인
    start = min(n, m)
    end = max(n, m)

    # 소수 개수 세기
    prime_count = 0

    for num in range(start, end + 1):
        if is_prime(num):
            prime_count += 1

    # 결과
    print(f"소수개수: {prime_count}")

# 두 개의 숫자 입력 받기
try:
    num1 = int(input("첫 번째 수 입력 : "))
    num2 = int(input("두 번째 수 입력 : "))

    count_prime_number(num1, num2)

except ValueError:
    print("알맞는 숫자를 적으세요.")
