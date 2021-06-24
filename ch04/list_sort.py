# 리스트의 최대값, 최소값, 정렬

score = [70, 80, 55, 60, 90, 40]
max = score[0]
n = len(score) # 6

for i in range(1, n):
    if max < score[i]:
        max = score[i]

print("최고 점수 %d" % max)

# 최저값은 max를 min으로 변경하면 됩니다.

# 오름차순 정렬 : 반대로 하면 내림 차순으로 됨
for i in range(0, n):
    for j in range(0, n-1):
        if score[j] > score[j+1]:
            score[j],score[j+1] = score[j+1], score[j]


for i in score:
    print(i, end=' ')

