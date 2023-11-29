from uuid import uuid4


class Product:
    def __init__(self, name: str, desc: str, price: float) -> None:
        self.__uuid: str = str(uuid4()).replace("-", "")
        self.__name: str = name
        self.__description: str = desc
        self.__price: float = price

    @property
    def uuid(self) -> str:
        return self.__uuid

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    def __eq__(self, other) -> bool:
        return self.uuid == other.uuid

    def __str__(self) -> str:
        return f"{self.__name} - {self.__description} - {self.__price:.2f}€"

    def __repr__(self) -> str:
        return f"Product(uuid={self.__uuid}, name={self.__name}, description={self.__description}, price={self.__price})"


class ShoppingCart:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def total_price(self) -> float:
        return sum([p.price for p in self.__products])

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, p: Product) -> None:
        self.__products.append(p)

    def remove_product(self, p: Product) -> None:
        self.__products = [product for product in self.__products if product != p]
