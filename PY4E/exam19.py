def good_customer(info):
    info_list = info.split(',')
    
    id_list = []
    age_list = []
    phone_list = []
    gender_list = []
    region_list = []
    purchase_count_list = []
    
    for i in range(0, len(info_list), 6):
        id_list.append(info_list[i])
        age_list.append(info_list[i+1])
        phone_list.append(info_list[i+2])
        gender_list.append(info_list[i+3])
        region_list.append(info_list[i+4])
        purchase_count_list.append(int(info_list[i+5]))
    
    vip_customers = {
        '아이디': [],
        '나이': [],
        '전화번호': [],
        '성별': [],
        '지역': [],
        '구매횟수': []
    }
    
    for i in range(len(id_list)):
        if purchase_count_list[i] >= 8 and phone_list[i] != 'x':
            vip_customers['아이디'].append(id_list[i])
            vip_customers['나이'].append(age_list[i])
            vip_customers['전화번호'].append(phone_list[i])
            vip_customers['성별'].append(gender_list[i])
            vip_customers['지역'].append(region_list[i])
            vip_customers['구매횟수'].append(purchase_count_list[i])
    
    print(vip_customers)
    
    for i in range(len(vip_customers['아이디'])):
        print(f"할인 쿠폰을 받을 회원정보 아이디:{vip_customers['아이디'][i]}, 나이:{vip_customers['나이'][i]}, 전화번호:{vip_customers['전화번호'][i]}, 성별:{vip_customers['성별'][i]}, 지역:{vip_customers['지역'][i]}, 구매횟수: {vip_customers['구매횟수'][i]}")

# 6명의 회원 정보
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

good_customer(info)
