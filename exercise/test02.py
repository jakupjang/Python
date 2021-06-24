# 교제 112쪽 연습문제
# Q1

국어 = 80
영어 = 75
수학 = 55

평균 = (국어 + 영어 + 수학) / 3

print("3개 과목의 합계는 %d점 입니다."% 평균)

# Q2

n = 13

if n % 2 == 0:
    print("짝수")
else:
    print("홀수")


# Q3

pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]

print(yyyymmdd)
print(num)

# Q4

pin = "881120-1068234"

성별 = int(pin[-7])

if 성별 == 1:
    print("남자")
else:
    print("여자")

print(type(pin))
print(type(성별))

# Q5

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6

a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# Q7

a = ['Life', 'is', 'too', 'short']
result = " ".join(a) # 문자열 합치기
resulta = a[0] + " " + a[1] + " " + a[2] + " " + a[3]
print(result)
print(resulta)

# split() 예제
s = "Life is too short"
s = s.split() #구분 기호 : 공백
print(s)

g = "a:b:c:d"
g = g.split(":")
print(g)


'''
# Q8
# 튜플 사용해야댐
a = (1, 2, 3)
a = a.append(4)
print(a)
'''
