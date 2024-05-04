# a= "dhjhdhjsjzhdhj"
# print(a.index("z"))

# flag = False
# text = 'hi my name is'
# if flag :
#     splited_text = text.split()
#     print(splited_text)
# else :
#     splited_text_list = text.split()
#     result = ""
#     for splited_text in splited_text_list:   #리스트형
#         result += splited_text
#     f = print(result)

# int1=1
# string1="안녕"
# list1=[1,2,3]
# dict1={"key" : "value"}
# tuple1=(1,2)
# bool1=True
# set1
# def add(a, b=4):
#     print(a+b)

# a = add(1,6)

# def aa():
#     return a

# print(aa())

def add_num(*args):
    result = 0
    for arg in args:
        result += arg
    return result
a = add_num(4,5,6)
print(a)

# add_num(3)

#a,b,flag flag가 + 문자일 경우 a+b flag x일 경우 a*b /result 메소드 제곱 /처음 메소드 값을 제곱 매서드에 넣고 제곱된것을 리턴 후 프린트

# def num(a,b,flag):
#     if flag == "+":
#         return a+b
#     elif flag == "x":
#         return a*b
# result = num(3,4,"+")
# print(result)  

# def num1(result):
#     return result ** 2
# re = num1(result)
# print(re)

# a=97
# print(f'a의 숫자는 {a} 입니다')
    
# def sub(a, b):
#      return a - b
# result = sub(7,5)
# print(result)

