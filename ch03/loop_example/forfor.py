# 충첩 for문

for i in range(1, 6):
    for j in range(1, 6):
        print("가", end=' ')
    print()

# 1부터 1씩 증가하기

for i in range(0, 6):
    for j in range(1, 6):
        num = i*5+j
        if num < 10:
            print("0%d"% num, end=' ')
        else:
            print(num, end= ' ')
    print()
