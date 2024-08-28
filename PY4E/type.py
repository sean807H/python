ddd=1+4
print(ddd)

eee='hello '+'world'
print(eee)

type(eee)   #class 'str' 문자열 클래스타입
type(1)     #정수 클래스타입

# eee=eee+1   #에러

#타입변환
i=42
type(i)     #int타입
f=float(i)  #float타입
print(f)    #42.0출력
type(f)     #float타입

sval='123'
type(sval)  #str타입
# print(sval+1)   #에러

ival=int(sval)
type(ival)  #int타입
print(ival+1)   #int타입 간 연산이기에 오류X

#입력
#print()=출력 input()=입력
nam=input('Who are you?')
print('Welcome',nam)
