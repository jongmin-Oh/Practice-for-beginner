#용이의 사랑 알고리즘
love = 100
print("김용 시크릿 주주의 사랑은 영원합니다.")
while True:
    life = int(input("김용의 전화를 몇 번 안 받았습니까? :"))
    if life == 0:
        print("김용이 평생의 복종의 맹세 서약 춤을 준비합니다.")
    elif life > 0 and life < 5:
        print("당신의 수명이 줄어듭니다. %d년 남았습니다." %(5 - life))
        love -= 10
    elif life >=5 and life < 10:
        print("당신은 큰 죄를 저질렀습니다. 돌이킬 수 없는 일이 다가옵니다.")
        love -= 30
    elif life >= 10:
        print("김용의 분노가 세상을 뒤덮습니다.")
        love = love - love
    if love <= 0:
        print("축하드립니다. 당신은 한달간 푸푸를 할 수 없습니다.")
        break