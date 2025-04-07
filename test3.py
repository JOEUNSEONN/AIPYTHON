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

# 그림 출력 3번 반복
for i in range(3):
    print(f"\n그림 출력 프로그램 ({i+1}/3)")
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
