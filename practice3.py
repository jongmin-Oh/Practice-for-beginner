## 3장 연습 1번은 너무 개쉬워서 2번부터하겠음
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

#3번
i = 0
while True:
    i += 1
    if i == 6 : break
    print('*' * (i))

#4번
for i in range(1,101):
    print(i)
#5번
middleterm = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in middleterm:
    total += score
average = total/len(middleterm)
print(average)
#6번
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
print(result)
#자 위의 코드를 내포를 이용해 표현해보자
numbers =[1,2,3,4,5]
result = [n*2 for n in numbers if n % 2 ==1]
print(result)

##4장
#1번
def is_odd(self):
    if self % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
is_odd(13)
is_odd(12)
#2번/숫자 평균 구하는 알고리즘
def what_avg(*number):
    result = 0
    for i in number:
        result = (result+i)
    return result/len(number)
what_avg(1,2,3,4,5,6,7,8)
#3번
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %d 입니다"% total)
#4번
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
#5번
with open("test.txt", 'w') as f1:
    f1.write("Life is too short")
f2 = open("test.txt", 'r')
print(f2.read())
#6번
def writing():
    contents = input("내용을 입력해 주세요. :")
    with open("test.txt", 'a') as f:
        f.write(contents)
        f.write("\n")
writing()
# user_input = input("저장할 내용을 입력하세요. :")
# with open("pcg.txt", 'a') as f:
#     f.write(user_input)
#     f.write("\n")
##7번 It's too hard
with open("test.txt", 'w') as f:
    f.write("Life is too short\nyou need python")
with open("test.txt", 'r') as ff:
    print(ff.read())
##5장
#1번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
class UpgradeCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def minus(self, val):
        self.value -= val
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
#2번
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value <= 50

    def add(self, val):

        self.value += val
cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력