import json

from src.models.shopping_cart import Product

DB: str = "src/db/data.json"


def get_product(uuid: str) -> Product | None:
    with open(DB, "r") as fd:
        while line := fd.readline():
            data: dict[str, str | float] = json.loads(line[:-1])
            if data["_Product__uuid"] == uuid:
                return Product(
                    uuid=data["_Product__uuid"],
                    name=data["_Product__name"],
                    desc=data["_Product__description"],
                    price=data["_Product__price"]
                )
    return None


def get_products() -> list[Product]:
    products: list[Product] = []
    with open(DB, "r") as fd:
        while line := fd.readline():
            data: dict[str, str | float] = json.loads(line[:-1])
            products.append(
                Product(
                    uuid=data["_Product__uuid"],
                    name=data["_Product__name"],
                    desc=data["_Product__description"],
                    price=data["_Product__price"]
                )
            )
    return products


def insert(p: Product) -> None:
    with open(DB, "a") as fd:
        fd.write(json.dumps(p.__dict__))
        fd.write("\n")
