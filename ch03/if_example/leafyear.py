# 윤년을 판별하는 프로그램

year = int(input("연도를 입력하세요 : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("%d년은 윤년 입니다."% year)
else:
    print("%d년은 윤년이 아닙니다."% year)
