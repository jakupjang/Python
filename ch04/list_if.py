# 리스트의 합격 판정
# 점수가 60점 이상이면 합격, 불합격

score = [70, 80, 50, 60, 90, 45]
index = 0

print("for - in 문 사용")
for i in score:
    index += 1
    if i >= 60:
        print("%d 합격" % index)
    else:
        print("%d 불합격" % index)

print('='*19)
print("for in range() 구문")

n = len(score)

for i in range(0, n):
    if score[i] >= 60:
        print("%d 합격" % (i+1))
    else:
        print("%d 불합격" % (i+1))
        
