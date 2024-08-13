def  make_comma(number):
    num_str = str(number)
    length = len(num_str)
    result = ""
    
    for i in range(length):
        result = num_str[length - 1 - i] + result
        if i % 3 == 2 and i != length - 1:
            result = "," + result
            
    return result

input_number = int(input("1,000 이상의 숫자를 입력하세요: "))
number =  make_comma(input_number)
print("3자리 나눈 숫자:", number)
