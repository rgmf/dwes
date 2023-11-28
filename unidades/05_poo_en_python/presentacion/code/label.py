
class Label:
    def __init__(self, text: str, font: str) -> None:
        self.__text: str = text
        self.__font: str = font

    def get_text(self) -> str:
        return self.__text

    def set_text(self, value: str) -> None:
        self.__text = value

    def get_font(self) -> str:
        return self.__font

    def set_font(self, value: str) -> None:
        self.__font = value


label: Label = Label("Etiqueta", "Fira Code")

text: str = label.get_text()
font: str = label.get_font()

label.set_text("Nuevo valor de Etiqueta")
label.set_font("Bitstream Vera Sans")


