# rich 아스키 코드 출력기
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.text import Text
from rich import box  # 테두리 스타일

console = Console()

# 각 동물 아스키 코드 정의 (raw string 사용!)
cat_art = r"""
 /\_/\  
( o.o ) 
 > ^ <  
"""

rabbit_art = r"""
 (\(\  
 ( -.-) 
 o_(")(")
"""

dog_art = r"""
  / \__
 (    @\____
 /         O
/   (_____/
/_____/   U
"""

def print_cute_ascii_art(choice):
    """선택에 따라 아스키 아트를 출력하는 함수"""
    if choice == 1:
        console.print(Align.center(
            Panel(cat_art, title="🐱 고양이", style="bold magenta", box=box.SQUARE, width=40)
        ))
    elif choice == 2:
        console.print(Align.center(
            Panel(rabbit_art, title="🐰 토끼", style="bold deep_pink4", box=box.SQUARE, width=40)
        ))
    elif choice == 3:
        console.print(Align.center(
            Panel(dog_art, title="🐶 강아지", style="bold yellow", box=box.SQUARE, width=40)
        ))
    else:
        console.print(Align.center("[red]⚠️ 잘못 입력했습니다. 1, 2, 3 중 하나를 입력해주세요.[/red]"))

def main():
    # 제목과 설명
    title = Text("🎨 아스키 코드 그림 출력기 🎨", style="bold cyan")
    subtitle = Text("번호를 선택해서 동물을 출력해보세요!", style="dim")

    console.print(Align.center(Panel(title, subtitle=subtitle, style="bold blue")))

    # 메뉴
    menu = Text()
    menu.append("1. 고양이 🐱\n", style="bold magenta")
    menu.append("2. 토끼 🐰\n", style="bold deep_pink4")
    menu.append("3. 강아지 🐶\n", style="bold yellow")
    menu.append("0. 종료 ❌\n", style="bold red")
    console.print(Align.center(menu))

    # 반복 입력
    while True:
        try:
            n = int(Prompt.ask("[bold green]선택[/bold green]", default="1"))
            if n == 0:
                console.print(Align.center("\n[bold red]프로그램을 종료합니다. 안녕! 👋[/bold red]"))
                break
            print_cute_ascii_art(n)
        except ValueError:
            console.print(Align.center("[red]숫자를 입력해주세요![/red]"))

if __name__ == "__main__":
    main()
