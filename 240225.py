# sp = ['a', 'b', 'c', 'd', 'e']
# result = sp.index('d')
# print(result)

# 김서연 : 1 / 박다슬 : 2 아이템을 뽑아서 key 박다슬은 value 를 프린트
# name = {"김서연" : 1, "박다슬" : 2}
# for k,v in name.items():
#     if k=="박다슬":
#         print(v)


# while 어떤 초기값 1 1부터 증가할떄 10까지 반복하는 것
# while!!!!!!!!!!!

class Test:
    def __init__(self, num):
        self.result = num

    def add(self, num):
        print(self.result)
        self.result += num

test = Test(1)
test.add(3)
