import random

def get_user_guess(previous_guesses, min_value, max_value):
    while True:
        try:
            guess = int(input("숫자를 예측해보세요 : "))
            if guess < min_value or guess > max_value:
                print(f"{min_value}부터 {max_value} 사이의 숫자를 입력하세요.")
                continue
            if guess in previous_guesses:
                print("이미 예측에 사용한 숫자입니다. 다시 한번 고민해보세요.")
                continue
            return guess
        except ValueError:
            print("숫자를 입력하세요.")

def compare_numbers(user_guess, target_number):
    if user_guess < target_number:
        return "UP"
    elif user_guess > target_number:
        return "Down"
    else:
        return "정답"

def guess_numbers():
    print("Up & Down 게임을 시작합니다!")
    print("---------------------------")

    target_number = random.randint(1, 100)
    previous_guesses = []
    min_value, max_value = 1, 100

    tries = 0
    closest_low = 100
    closest_high = 1

    while True:
        tries += 1
        user_guess = get_user_guess(previous_guesses, min_value, max_value)
        previous_guesses.append(user_guess)

        result = compare_numbers(user_guess, target_number)
        print(f"\n{tries}차 시도")
        print(f"숫자를 예측해보세요 : {user_guess}")
        print(result, end=" ")
        if result == "UP":
            max_value = user_guess - 1
            print("다시 한번 고민해보세요.")
        elif result == "Down":
            min_value = user_guess + 1
            print("다시 한번 고민해보세요.")
        else:
            print(f"{tries}차 시도만에 예측에 성공했네요!! 게임을 종료합니다.")
            break

        if user_guess < closest_low:
            closest_low = user_guess
            print(f"지금까지의 시도 중 정답에 가까운 최소값은 {closest_low}입니다.")
        if user_guess > closest_high:
            closest_high = user_guess
            print(f"지금까지의 시도 중 정답에 가까운 최대값은 {closest_high}입니다.")

if __name__ == "__main__":
    guess_numbers()
