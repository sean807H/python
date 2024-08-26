x=5
if x<10:   #콜론중요!
    print('smaller')
else:
    print('bigger')

y=21
if y<2:
    print('small')
elif y<10:  #조건문 추가
    print('medium')
elif y<20:
    print('big')
else:
    print('ginormous')

astr="123"
try:
    print("hello")
    islnt=int(astr)
    print("world")
except:
    islnt="integer로 변환할 수 없습니다."
print('done',islnt)