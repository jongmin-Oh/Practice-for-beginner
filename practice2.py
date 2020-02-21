#실습이야 정신차리자
#과일 숫자 세는 프로그램 만들어 보자
fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아","복숭아","복숭아"]

d = {}

for f in fruit:
    if f in d: #"사과"라는 key가 d라는 딕셔너리에 있어?
        d[f] = d[f] + 1 #그럼 "사과" 갯수를 하나 올려줘
    else:
        d[f] = 1 #만약 "사과"라는 애가 없으면, 그걸 딕셔너리에 넣고 벨류는 1로 만들어줘

print(d)

##클래스와 오브젝트에 대해 araboja
#클래스:함수와 변수의 합
#오브젝트: 클래스를 이용해서 만든 것
#클래스->빵틀, 오브젝트->빵
#오브젝트를 인스턴트라고도 한다.

class Person:
    def say_hello(self):
        print("안녕!")

p = Person()
p.say_hello()

#이번엔 변수도 클래스에 넣어보자
#person에 이름을 할당하고
class Person:
    name = "종민"

    def say_hello(self):
        print("안녕! 나는 " + self.name)

p = Person()
p.say_hello()

#만약 내가 여러 명의 person을 만들고 싶다면
class Person:
    name = "종민"

    def say_hello(self):
        print("안녕! 나는 " + self.name)

jongmin = Person()
dayoung = Person()
jenny = Person()
jongmin.say_hello()
dayoung.say_hello()
jenny.say_hello()
#내가 이미 name에 "종민"을 할당했으니
#"name"변수를 "종민"으로 fix하지 않고 오브젝트를 만들 때 지정하고 싶다
#자 그러면 새로운 함수를 써야한다
#이름하여 __init__

class Person:
    def __init__(self, name):#자 name이라는 인자가 있고
        self.name = name#그 인자에 변수를 받아서 할당해라

    def say_hello(self):
        print("안녕! 나는 " + self.name)

jongmin = Person("jongmin")
dayoung = Person("dayoung")
jenny = Person("jenny")
jongmin.say_hello()
dayoung.say_hello()
jenny.say_hello()

#이번엔 say_hello함수에 인자 하나를 추가하자
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 " + self.name)

jongmin = Person("jongmin")
dayoung = Person("dayoung")
jenny = Person("jenny")
jongmin.say_hello("파이썬")
dayoung.say_hello("세무사")
jenny.say_hello("로제")

#이번엔 age인자를 추가하자

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 " + self.name)

    def introduce(self):
        print("안녕? 내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")

jongmin = Person("jongmin", 26)
jongmin.introduce()

##상속도 배워보자
#공통된 클래스가 있고 좀 다른 여러 세부 클래스를 새로 만들고 싶을 때
#가령 person이 있는데 경찰이나 개발자 클래스를 만들고 싶다면
#이때 경찰이 할 수 있는건 개발자랑 달라야 하고
#경찰이나 개발자가 person이 할 수 있는건 다 할 수 있어야 한다.

    class Police(Person):
        def arrest(self, to_arrest):
            print("넌 체포됐다, " + to_arrest)
#이게지금 무슨 상황이냐면 Police가 Person을 상속하므로써 Person의 함수들을
#계승한 상황. 즉, Police(Person)이란 것은 사실
# class Police:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self, to_name):
#         print("안녕! " + to_name + " 나는 " + self.name)
#
#     def introduce(self):
#         print("안녕? 내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")
#라고 한 것과 완전히 동일한 것이다.
#우리는 Police에 Person을 상속하므로써 저 코드들을 skip할 수 있는 것


    class Programmer(Person):
        def program(self, to_program):
            print("다음엔 뭘 만들지? 아 이걸 만들어야겠다:" + to_program)

    jongmin = Person("종민", 26)
    dayoung = Police("다영", 24)
    jenny = Programmer("제니", 20)

jenny.introduce()
dayoung.introduce()

dayoung.arrest("종민")
jenny.program("이메일 클라이언트")

#만약 dayoung에게 program시키거나 jenny에게 arrest시키면 오류.
#서로할 줄 아는 건 다른 거고 상속받은 함수들은 공통으로 쓸 수 있다!
#열심히 복습하자.......

#1~1000까지의 소수 출력 프로그램
n=1000
a = [False,False] + [True]*(n-1)
finder=[]

for i in range(2,n+1):
  if a[i]:
    finder.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(finder)


#에러를 만드는 함수 실습
shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration #에러를 만드는 함수
except StopIteration:
    print("풀은 {}원입니다.".format(price))

##class / object 실습
class animal():
    def __init__(self, name):
        self.name = name
    def run(self):
        print("{}가 달립니다.".format(self.name))
    def eat(self):
        print("{}가 먹습니다.".format(self.name))


class dog(animal):

    def bark(self):
        print("{}가 짖습니다.".format(self.name))

a = dog("야호")
a.run()
a.eat()
a.bark()
#문자열 연습?
"%10s" % "hi"
"%-10s다영" % "hi"

age = 25
f'나는 올 해 {age + 1}살이 된다.'

#반복문 실습
f = ["korea", "korea", "japan", "japan", "asia", "usa", "eurupe", "german", "german", "usa", "usa"]
a= {}
for i in f:
    if i in a:
        a[i] = a[i] + 1
    else:
        a[i] = 1
print(a)

#while문 실습
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 {}번 찍었습니다.".format(treeHit))

    if treeHit == 10:
        print("나무가 넘어갑니다.")

#또 실습
understand = 0
while understand < 4:
    understand = understand + 1
    print("%d번 참았다....." % understand)
    if understand == 4:
        print("인내심이 한계에 도달하였습니다.")

인내심 = 10
종민 = "person"
while 종민:
    인내심 = 인내심 - 1
    print("{}번 남았습니다. 인내심이 바닥나고 있습니다.".format(인내심))
    if 인내심 == 0:
        print("축하드립니다. 인내심이 바닥났습니다.")
        break
#제어문 실습
coffee = 10
while True:
    money = int(input("금액을 넣어 주세요."))
    if money == 300:
        print("커피가 나오고 있습니다.")
        coffee = coffee -1
    elif money > 300:
        print("잔돈 %d원을 받아주세요. 잔돈 수령 후 커피가 나옵니다." % (money - 300))
        coffee = coffee -1
    else:
        print("금액을 반환합니다.")
        print("남은 커피의 양은 %d개입니다." %coffee)
    if coffee == 0:
        print("제품이 모두 소진되었습니다. 판매를 중지합니다.")
        break

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

#연습문제 2장 1번
grade = {"국어": 80, "영어": 75, "수학": 55}
j = 0
for i in grade.values():
    j=(j+i)
print(j/3)

#연습문제 2장 2번
while True:
    classifier = int(input("분류하고자 하는 수를 입력하십시오 : "))
    if classifier % 2 == 0:
        print("해당 숫자는 짝수입니다.")
    else :
        print("해당 숫자는 홀수입니다.")

#연습문제 2장 3번
pin = "881120 - 1068234"
yyyymmdd = pin[:6]
num = pin[9:]
print(yyyymmdd)
print(num)

#연습문제 2장 4번
while True:
    pin = str(input("당신의 주민등록번호를 입력하세요 :"))
    yyyymmdd = pin[:6]
    num = pin[6:]
    if num[0] == str(1):
        print("당신은 남성입니다.")
    elif num[0] == str(2):
        print("당신은 여성입니다.")
    else:
        print("잘못 입력하였습니다. 다시 입력해주세요.")

#연습문제 2장 5번
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#연습문제 2장 6번
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#연습문제 2장 7번
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) #문자열 합치는 join 함수 이용법 알아두기
print(result)

#연습문제 2장 8번
a= (1,2,3)
a = a + tuple(4)
print(a)   # 모르겠음 pass

#연습 2장 9번
a = dict()
a
a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python'
a[250] = 'python'
#오류가 나는 경우는 3번 a[[1]]일 때. 왜냐면 딕셔너리의 key로 list는 올 수 없거든.

#연습문제 2장 10번
a= {'A':90, 'B':80, 'C':70}
result = a['B']
print(a)
print(result)

#연습 2장 11번
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#연습 2장 12번
a = b = [1,2,3]
a[1] = 4
print(b)
#하나의 코드 안에 a=b=[1,2,3] 이라고 했으니 a를 update한 것은 b를 한 것 과 마찬가지




