# 사용자로부터 입력을 받는 함수
def print_multiplication_table():
    # 사용자에게 숫자를 입력받습니다.
    number = int(input("구구단을 출력할 숫자를 입력하세요 (예: 2): "))

    # 구구단 출력
    print(f"\n{number}단 출력:")
    for i in range(1, 10):
        print(f"{number} x {i} = {number * i}")

# 프로그램 실행
print_multiplication_table()
