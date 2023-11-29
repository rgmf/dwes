from src.shopping_cart import Product, ShoppingCart


def test_all():
    pa: Product = Product("a", "aaa", 1.25)
    pb: Product = Product("b", "bbb", 2.25)
    pc: Product = Product("c", "ccc", 3.25)
    pd: Product = Product("d", "ddd", 4.25)
    sc: ShoppingCart = ShoppingCart()

    # 2 a
    sc.add_product(pa)
    assert len(sc.products) == 1

    sc.add_product(pa)
    assert len(sc.products) == 2

    # 2 b
    sc.add_product(pb)
    assert len(sc.products) == 3

    sc.add_product(pb)
    assert len(sc.products) == 4

    # 1 c
    sc.add_product(pc)
    assert len(sc.products) == 5

    # Remove all 2 b
    sc.remove_product(pb)
    assert len(sc.products) == 3

    # Remove d that is not in sc
    sc.remove_product(pd)
    assert len(sc.products) == 3

    # Remove all 2 b that not exists yet
    sc.remove_product(pb)
    assert len(sc.products) == 3

    # Remove c
    sc.remove_product(pc)
    assert len(sc.products) == 2

    # Remove 2 a
    sc.remove_product(pa)
    assert len(sc.products) == 0

    # Remove 2 a that not exists yes
    sc.remove_product(pa)
    assert len(sc.products) == 0
