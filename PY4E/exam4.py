import random

def rcp(my):
    computer = random.choice(["가위", "바위", "보"])

    print(f"나: {my}")
    print(f"컴퓨터: {computer}")

    if my == computer:
        print("무승부!")
    elif my == "가위" and computer == "보":
        print("사용자 승리!")
    elif my == "바위" and computer == "가위":
        print("사용자 승리!")
    elif my == "보" and computer == "바위":
        print("사용자 승리!")
    else:
        print("컴퓨터 승리!")

if __name__ == "__main__":
    my = input("가위 바위 보").lower()
    rcp(my)
