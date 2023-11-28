class Label:
    def __init__(self, text: str, font: str) -> None:
        self.__text: str = text
        self.__font: str = font

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value: str) -> None:
        self.__text = value

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, value: str) -> None:
        self.__font = value

    def __str__(self) -> str:
        return f"Etiqueta: {self.text} ({self.font})"

    def __repr__(self) -> str:
        class_name: str = type(self).__name__
        return f"<{class_name} (text: {self.text}, label: {self.font})>"


label: Label = Label("Etiqueta", "Fira Code")

text: str = label.text
font: str = label.font

label.text = "Nuevo valor de Etiqueta"
label.font = "Bitstream Vera Sans"
