##타입의 종류
# 1.숫자 2.문자 3.불리안(True or False)
# 1.숫자
x = 1
y = 2
z = 1.2

print(x)
print(y)
print(z)

print(x + y)
print(z - x)

print(x * z)
print(x % z)

8/3

14//3
# 2.문자

x = "종민"
y = '천재'

print(x)
print(y)


z  =  "안녕하세요다영이 남자친구입니다"
"문자열"
""
print(z)


print("안녕" + " 잘 지내니")
print("너 몇살이니" + 4)  #같은 타입 끼리 해야함

print("너 몇살이니" + str(4)) #이것을 캐스팅이라고 함




#다른 예시

x = 4
y = "4"

print(str(x) + y)  #숫자를 문자타입으로
print(x + int(y))  #문자를 숫자타입으로

# 3.불리안  boolean

x = True
y = False

print(x)
print(y)
#index와 slicing
a = "Life is too short, you need python"
len(a)
a[3]
a[-4]
b = a[0] + a[1] + a[2] + a[3]
b
b = a[0:4]
# 조건문
if 2 > 1:
    print("Hello")

if not 1 > 2:
    print("Hello")

if 1>0 and 2>1:
    print("Hello")

if 0>0 or 2>1:
    print("Hello")
# else에 관해
x = 3

if x > 5:
    print("Hello")
else:
    print("Hi")

# else if -> elif에 관해

x = 3


if x > 5:
    print("Hello")
elif x == 3:
    print("Bye")
else:
    print("Hi")

## 반복문 function

def chat():
    print("알렉스: 안녕? 넌 몇 살이니?")
    print("윤하: 나? 나는 20")
chat()
# string : 문자열
## 좀 더 심화

def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age))
float

chat("알렉스", "윤하", 10)
chat("종민", "다영", 20)
str(4)

## 난 왜 안 돼는가



print("화이팅 오종민")

print("오종민\n오종민\n오종민")

# 1. 함수는 tab을 기준으로 인식한다. 그래서 함수를 정의할 때 정의 부분까지만 Tab으로 써야한다.
# 2. 줄을 나눌 때는 \n 을 쓰자
# 3. 문자열은 string(str()함수, %s 모두 string)이고 영어 알파벳 하나가 1byte --> 한글은 당연히 2byte겠지?
# 4. 굳이 띄어쓰지 않아도 되면 띄어쓰지 말자
# 5. ""는 공백 문자열이야. """는 주석의 시작을 알리는 거

    def sayhello(name, age):
        if age < 10:
            print("안녕," + name)
        elif age <= 20 and age >=10:
            print("안녕하세요," + name)
        else:
            print("안녕하십니까," + name)

    sayhello("종민", 20)
    sayhello("준형", 30)
    sayhello("하랑", 7)

##반복문
#for

for a in [1,2,3]:
    print(a)

i=0
while i < 3:
    i = i+1
    print(i)

 for i in range(3):
     print("종민: 안녕, 다영아 뭐해?")
     print("다영: 알 것 없잖아?")
#for i 라는 건 i에 몇번째인지 변수를 넣으라는 소리. range 수만큼 반복해라 // 코딩을 하다보면 알겠지만 i는 0부터 시작한다.
#이것을 for loop 라고 함


#while
#while은 조건을 달 수 있음

    i=0
    while i < 3:
        print("종민: 다영아 뭐해")
        print("다영: 뭘봐")
        i = i+1

#기본적으로 for while 호환되나
#각 각으로 쓰는게 편할 때가 있다

#while > for 인 경우
#무한루프일 때

    i = 0
    while True:
        print("종민: 다영아 뭐해")
        print("다영: 뭘봐")
        i = i + 1

#영원히 끝나지 않는 #고통의 쳇바퀴
#끊고싶다면 #break #continue

i = 0
    while True:
        print("종민: 다영아 뭐해")
        print("다영: 뭘봐")
        i = i + 1

        if i>2:
            break

#for로 표현한다면
    for i in range(100):
        print("종민:바보")
        print("다영:그건 너")

        if i > 2:
            break

#continue의 활용

    for i in range(3):
        print("안녕 클레오파트라")
        print("세상에서 제일 가는")

        continue

        print("스트라이커")

#즉 continue 밑으로 가지 않고 처음으로. 도돌이표같은 느낌

for i in range(3):
    print("안녕 클레오파트라")
    print("세상에서 제일 가는")

    if i == 1:
        continue

    print("스트라이커")

##드디어 자료구조
#리스트, 튜플, 딕셔너리

#리스트
x=list()
y=[]
#이 두개는 #젖가락 두 짝

x=[1,2,3,4]
y=["hello", "world"]

print(x+y)
#즉, elementry를 grouping하는 것
x=[1,2,3,4]
print(x[3])
#i는 0부터 시작하니까#3번째는 4

x[3] = 10
print(x)
#원소 바꿔치기

x=[1,2,3,4]
num_elements = len(x)
print(num_elements)
#리스트의 크기를 구하는 것

x=[4,2,3,1]

y = sorted(x)
print(y)
z = sum(x)
print(z)

#반복문과 짬뽕

x = [4,2,3,1]
y = ["hello", "there"]

for n in x:
    print(n)

for c in y:
    print(c)

#난 왜 안 돼는가

#엘리멘탈 위치 찾기
#index 이용

x=[4,2,3,1]
y=["hello", "there"]

print(x.index(3))
print(y.index("hello"))

#넌 또 뭐가 문제야

#엘리멘트가 어디 있는지는 관심없고 있는지만 알고 싶을 때
print("hello" in y)

print("bye" in y)

#조건문과 합쳐보쟈

y=["hello", "there"]

if "hello" in y:
    print("hello 가 있어요")


##튜플

x=(1,2,3)
y=('a','b','c')
z=(1,"hello","there")

print(x+y)
print('a' in y)
print(z.index(1))

##리스트에서 쓰는 거의 대부분 func이 가능
##대표적으로 안 되는건 assignment
##튜플 안의 원소를 바꾸는게 안됨
##즉 리스트는 mutable, 튜플은 immutable

x[0] = 10

##딕셔너리

x=dict()
y={}

#위 두개는 똑같음
#딕셔너리는 key와 value로 이루어져 있다

x = {
    "name": "종민",
    "age": 26,
}

print(x)
print(x["name"])
print(x["age"])

#"name"이라는 key에 있는 value를 물은 것
#"age"라는 key에 있는 value를 물은 것
#이 때 key는 불변(문자열, 숫자같은)이다. immutable
#즉 리스트는 딕셔너리의 key로 쓸 수 없다.

x = {
    0: "jongmin",
    1: "Hello",
    "age": 20
}
print(x[0])
print(x[1])
print(x["age"])

#그리고 어떤 key가 있는지 확인가능

print("age" in x)
print("name" in x)

print(x,keys())
print(x,values())
#x의 key들을 보여주세요
#x의 value들을 보여주세요
#근데 난 왜 안 되요?

#반복문과 결합
x = {
    0: "jongmin",
    1: "Hello",
    "age": 20
}
for key in x:
    print(key)
    print(x[key])

#혹은
for key in x:
    print("key: " + str(key))
    print("value: " + str(x[key]))

#딕셔너리도 assign 가능
x = {
    0: "jongmin",
    1: "Hello",
    "age": 20
}
x[0]="종민"
print(x)
#새로운 key와 그에 따른 value도 할당가능

x["school"] = "Yonsei"
print(x)
