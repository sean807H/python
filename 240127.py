# key : 1, value : 김서연
# key : 2, value : 박은수
# a = c
# for k, v in a.items():
#     print(f'key : {k}, value : {v}')

# # vartest.py
# a = 1
# def vartest(a):
#     a = a +1
#     return a
# a = vartest(a)
# print(a)








































# # key : 1, value : 김서연
# # key : 2, value : 박은수
# 입력값 딕션러니 출력값 프린트값(리스트로 만들어서 리턴) ["key : 1, value: 김서연" ,"key : 2, value: 박은수"]
def name(input_dict):
    result_list = list()
    for k, v in input_dict.items():
        result_list.append(f'key : {k}, value : {v}')
    return result_list
#입력, 호출
input_dict = {1 : '김서연', 2 : '박은수'}
result = name(input_dict)
print(result)

# 계산기를 만들거야/ 계산기는 플마곱나 이걸 다 메소드로 만들고 3이랑 7을 입력받아서 하나하나하나를 다 결괏값을 보여주면돼
# def add(add_num1, add_num2):
#     return add_num1+add_num2
# def sub(sub_num1, sub_num2):
#     return sub_num1-sub_num2
# def mul(mul_num1, mul_num2):
#     return mul_num1*mul_num2
# def div(div_num1, div_num2):
#     return div_num1/div_num2

# input_1 = 3
# input_2 = 7
# add=add(input_1,input_2)
# sub=sub(input_1,input_2)
# mul=mul(input_1,input_2)
# div=div(input_1,input_2)
# print(add)
# print(sub)
# print(mul)
# print(div)

# a = input()