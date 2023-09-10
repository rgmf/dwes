"""Module with functions to draw the UI."""
from rich import box
from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.console import Group
from rich.prompt import Prompt

# All gallow positions.
BEGIN_GALLOW = "[bold green]+---+\n|   |\n|   [/bold green][bold red]O[/bold red][bold green]\n|"
GALLOW = [
    "[bold green]+---+\n|   |\n|\n|\n|\n|\n========[/bold green]",
    f"{BEGIN_GALLOW}\n|\n|\n========[/bold green]",
    f"{BEGIN_GALLOW}   [/bold green][bold red]|[/bold red][bold green]\n|\n|\n========[/bold green]",
    f"{BEGIN_GALLOW}  [/bold green][bold red]/|[/bold red][bold green]\n|\n|\n========[/bold green]",
    f"{BEGIN_GALLOW}  [/bold green][bold red]/|\\ [/bold red][bold green]\n|\n|\n========[/bold green]",
    f"{BEGIN_GALLOW}  [/bold green][bold red]/|\\ [/bold red][bold green]\n|  [/bold green][bold red]/[/bold red][bold green]\n|\n========[/bold green]",
    f"{BEGIN_GALLOW}  [/bold green][bold red]/|\\ [/bold red][bold green]\n|  [/bold green][bold red]/ \\ [/bold red][bold green]\n|\n========[/bold green]"
]


def make_layout() -> Layout:
    """Define the layout."""
    new_layout = Layout(name="root")

    new_layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )
    new_layout["main"].split_row(
        Layout(name="side"),
        Layout(name="hint", ratio=2, minimum_size=60),
    )
    new_layout["side"].split(Layout(name="letters"), Layout(name="gallow"))
    return new_layout


class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        # grid.add_column(justify="right")
        grid.add_row(
            "El [b]Ahorcado[/b] Retro Game",
            # datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")


def make_final_panel(mesg: str) -> Panel:
    """Make a Panel with the message."""
    panel = Panel(
        Align.center(
            Group("\n", Align.center(mesg)),
            vertical="middle"
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="Gallow",
        border_style="bright_blue"
    )
    return panel


def make_gallow(attempt: int) -> Panel:
    """Make a Panel with the gallow in the attempt."""
    gallow_panel = Panel(
        Align.center(
            Group("\n", Align.center(GALLOW[attempt])),
            vertical="middle"
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="Gallow",
        border_style="bright_blue"
    )
    return gallow_panel


def make_hint(hint: str) -> Panel:
    """Make a Panel with the hint for guessing the sentence."""
    hint_panel = Panel(
        Align.center(
            Group("\n", Align.center(hint)),
            vertical="middle"
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="Pista",
        border_style="bright_blue"
    )
    return hint_panel


def make_letters(letters: list[str]) -> Panel:
    """Make a Panel with the hint for guessing the sentence."""
    letters_panel = Panel(
        Align.center(
            Group("\n", Align.center(", ".join(letters))),
            vertical="middle"
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="Letras usadas",
        border_style="bright_blue"
    )
    return letters_panel


def make_footer(text: str, error: bool) -> Panel:
    """Make a Panel with the text."""
    text = (
        f"{'[bold red]'}{text}{'[/bold red]'}" if error else 
        f"{'[bold green]'}{text}{'[/bold green]'}"
    )
    footer_panel = Panel(
        Align.center(
            Group("\n", Align.center(text)),
            vertical="middle"
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="Información",
        border_style="bright_blue"
    )
    return footer_panel


# Rich layout.
layout = make_layout()
layout["header"].update(Header())
layout["gallow"].update(make_gallow(0))
layout["letters"].update(make_letters([]))
layout["footer"].update(make_footer("Bienvenid@ al juego... ¡suerte!", False))


def ui_show_info(info: str, error: bool = False) -> None:
    global layout
    layout["footer"].update(make_footer(info, error))
    print(layout)


def ui_hint(hint: str) -> None:
    global layout
    layout["hint"].update(make_hint(hint))
    print(layout)


def ui_gallow(attempt: int) -> None:
    global layout
    layout["gallow"].update(make_gallow(attempt))
    print(layout)


def ui_letters(letters: list[str]) -> None:
    global layout
    layout["letters"].update(make_letters(letters))
    print(layout)


def ui_ask(question: str) -> str:
    global layout
    letter: str = Prompt.ask(question)
    print(layout)
    return letter


def ui_ask_for_sentence() -> str:
    global layout
    sentence: str = Prompt.ask("¿Qué frase es? ('c' si no la sabes para continuar) ")
    print(layout)
    return sentence


def ui_game_over() -> None:
    new_layout = Layout(name="root")
    new_layout["root"].update(
        make_final_panel(
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀┼┼┼┼┼███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼┼\n"
            "┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼┼\n"
            "┼██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼┼\n"
            "┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼┼\n"
            "┼███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄┼┼┼┼┼███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██████████████          ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ████       ███          ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██         ███          ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██        /   \\         ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██        \\___/         ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██         |||          ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██       //|||\\\\        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██      // ||| \\\\       ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██         ===          ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██         ===          ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██        // \\\\         ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██       //   \\\\        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██      //     \\\\       ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██                      ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██                      ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼   ██████████████████████  ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"
        )
    )
    print(new_layout)


def ui_error() -> None:
    new_layout = Layout(name="root")
    new_layout["root"].update(
        make_final_panel(
            "1001001010010010100100101001001010010010100100101001001010010010100100101001001\n"
            "1001001010010010100100101001001010010010100100101001001010010010100100101001001\n"
            "10010010100100110██████1███████101███████101██████01███████10010010100100100101\n"
            "10010010100100110██ 1001██10 ██101██10 ██101██1 ██01██01 ██10010010100100100101\n"
            "10010010100100110████ 10██10 ██101██10 ██101██0 ██01██01 ██10010010100100100101\n"
            "10010010100100110██ 1001██████1101██████1101██1 ██01██████100100101001001001010\n"
            "10010010100100110██████1██1 ████01██0 ████01██████01██ 1████1001001010010010010\n"
            "1001001010010010100100101001001010010010100100101001001010010010100100101001001\n"
            "1001001010010010100100101001001010010010100100101001001010010010100100101001001"
        )
    )
    print(new_layout)


def ui_win() -> None:
    new_layout = Layout(name="root")
    new_layout["root"].update(
        make_final_panel(
            "has acertado has acertado has acertado has acertado has acertado has acertado h\n"
            "has acertado has acertado has acertado has acertado has acertado has acertado h\n"
            "has acertado has acertad██████a██r██████a████erta██ has acertado has acertado h\n"
            "has acertado has acertad██ha██a██r██do ha██a██rta██ has acertado has acertado h\n"
            "has acertado has acertad██████a██r████ ha██ac██ta██ has acertado has acertado h\n"
            "has acertado has acertad██ha██a██r██do ha██ace██a██ has acertado has acertado h\n"
            "has acertado has acertad██████a██r██████a██acer████ has acertado has acertado h\n"
            "has acertado has acertado has acertado has acertado has acertado has acertado h\n"
            "has acertado has acertado has acertado has acertado has acertado has acertado h\n"
        )
    )
    print(new_layout)
