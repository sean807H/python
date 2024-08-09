def gugudan(num):
    if num <= 50:
        for i in range(1, 10, 2):
            result = num * i
            print(f"{num} x {i} = {result}")

try:
    number = int(input("몇 단? : "))
    gugudan(number)
except ValueError:
    print("알맞은 숫자를 적어주세요.")
    