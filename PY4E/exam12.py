import random

def player_turn(current_number):
    while True:
        try:
            input_numbers = input("My turn - 숫자를 입력하세요: ")
            input_numbers = [int(num) for num in input_numbers.split()]
            if not (1 <= len(input_numbers) <= 3):
                print("한 번에 1~3개의 숫자를 입력하세요.")
                continue
            valid_input = all(num == current_number + i for i, num in enumerate(input_numbers))
            if not valid_input:
                print("올바른 규칙에 맞지 않는 숫자입니다. 다시 입력하세요.")
                continue
            return input_numbers[-1]
        except ValueError:
            print("숫자를 입력해주세요.")

def computer_turn(current_number):
    max_computer_choice = min(3, 31 - current_number)
    computer_choice = random.randint(1, max_computer_choice)
    return current_number + computer_choice

def bs31():
    print("베스킨 라빈스 31 게임")
    print("------------------")
    
    current_number = 1
    player_turns = True 
    
    while current_number < 31:
        if player_turns:
            print(f"현재 숫자 : {current_number}")
            current_number = player_turn(current_number)
            player_turns = False
        else:
            print(f"현재 숫자 : {current_number}")
            current_number = computer_turn(current_number)
            player_turns = True
    
    if player_turns:
        print("컴퓨터 승리!")
    else:
        print("플레이어 승리!")

if __name__ == "__main__":
    bs31()
