# 동물 그림 출력 프로그램이 총 5번 반복 실행될 수 있게 만드시오.

# 아스키 코드 그림 출력하기

def print_cat():
    cat = [
        " /\_/\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    for line in cat:
        print(line)

def print_rabbit():
    rabbit = [
        " (\\(\\  ",
        " ( -.-) ",
        " o_(\")(\")"
    ]
    for line in rabbit:
        print(line)

def print_dog():
    dog = [
        " / \\__",
        "(    @\\____",
        " /         O",
        "/   (_____/",
        "/_____/   U"
    ]
    for line in dog:
        print(line)

def print_cute_ascii_art(n):
    if n == 1:
        print_cat()
    elif n == 2:
        print_rabbit()
    elif n == 3:
        print_dog()
    else:
        print("잘못 입력했습니다. 1, 2, 3 중 하나를 입력해주세요.")

# 그림 출력 5번 반복
for i in range(5):
    print(f"\n그림 출력 프로그램 ({i+1}/5)")
    print("-----------------")
    print("1. 고양이")
    print("2. 토끼")
    print("3. 강아지")
    print("-----------------")

    try:
        n = int(input("선택: "))
        print_cute_ascii_art(n)
    except ValueError:
        print("숫자를 입력해주세요.")

# 위 프로그램을 완성한 사람은 프로그램이 계속(무한) 반복하게 하고
# 만약에 0을 입력하면 종료 되는 프로그램을 만드시오

# 아스키 코드 그림 출력하기

def print_cat():
    cat = [
        " /\_/\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    for line in cat:
        print(line)

def print_rabbit():
    rabbit = [
        " (\\(\\  ",
        " ( -.-) ",
        " o_(\")(\")"
    ]
    for line in rabbit:
        print(line)

def print_dog():
    dog = [
        " / \\__",
        "(    @\\____",
        " /         O",
        "/   (_____/",
        "/_____/   U"
    ]
    for line in dog:
        print(line)

def print_cute_ascii_art(n):
    if n == 1:
        print_cat()
    elif n == 2:
        print_rabbit()
    elif n == 3:
        print_dog()
    else:
        print("잘못 입력했습니다. 1, 2, 3 중 하나를 입력해주세요.")

# 무한 반복 + 0 입력 시 종료
while True:
    print("\n그림 출력 프로그램")
    print("-----------------")
    print("1. 고양이")
    print("2. 토끼")
    print("3. 강아지")
    print("0. 종료")
    print("-----------------")

    try:
        n = int(input("선택: "))
        if n == 0:
            print("프로그램을 종료합니다.")
            break
        print_cute_ascii_art(n)
    except ValueError:
        print("숫자를 입력해주세요.")
