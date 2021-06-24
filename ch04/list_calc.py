# 리스트의 연산

score = [70, 80, 55, 60, 90, 40]


count = len(score) #len() 리스트 갯수 출력
sum = 0

# 합계
for i in score:
    sum += i
    print("i=%d, sum=%d" % (i, sum))

print("갯수 : %d" % count)
print("합계 : %d" % sum)

# 평균
avg = sum / count

print("평균 : %.2f" % avg) #%.1f = 소수점 첫번쨰까지 출력

