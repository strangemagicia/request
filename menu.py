from random import choice
kor = ['김치찌개', '된장찌개', '순두부찌개']
eng = ['토마토파스타', '알리오올리오', '토마토스튜']
chn = ['짜장', '짬뽕', '마파두부']
jpn = ['우동', '덮밥', '오차즈케']
menu = input('오늘은 무슨 메뉴?')
if menu == '한식':
    print(choice(kor))
    breakpoint()
elif menu == '중식':
    print(choice(chn))
    breakpoint()
elif menu == '양식':
    print(choice(eng))
    breakpoint()
else:
    print(choice(jpn))
