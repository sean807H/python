import random

def rcp(my, computer):
    print(f"나: {my}")
    print(f"컴퓨터: {computer}")

    if my == computer:
        print("무승부!")
        return "무승부"
    elif (my == "가위" and computer == "보") or \
         (my == "바위" and computer == "가위") or \
         (my == "보" and computer == "바위"):
        print("사용자 승리!")
        return "사용자 승리"
    else:
        print("컴퓨터 승리!")
        return "컴퓨터 승리"

def play(total):
    win = 0
    computer_win = 0
    ties = 0

    for i in range(1, total + 1):
        print(f"\n가위 바위 보 : {i} 번째 판")
        while True:
            user = input("가위 바위 보 중 하나를 선택하세요 (가위/바위/보): ").strip().lower()
            if user in ["가위", "바위", "보"]:
                break
            else:
                print("잘못된 입력입니다. 다시 선택하세요.")

        computer = random.choice(["가위", "바위", "보"])
        result = rcp(user, computer)

        if result == "무승부":
            ties += 1
        elif result == "사용자 승리":
            win += 1
        else:
            computer_win += 1

    print("\n=== 최종 결과 ===")
    print(f"나의 전적: {win}승 {ties}무 {computer_win}패")
    print(f"컴퓨터의 전적: {computer_win}승 {ties}무 {win}패")


try:
    while True:
        total = int(input("몇 판을 진행하시겠습니까? : "))
        if total <= 0:
            print("1 이상의 숫자를 입력하세요.")
        else:
            play(total)
            break
except ValueError:
    print("알맞은 숫자를 입력하세요.")
