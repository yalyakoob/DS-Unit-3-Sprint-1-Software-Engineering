# !/usr/bin/env python


from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price():
    """Test default product price being 10."""
    prod = Product("Test Product")
    assert prod.price == 10


def test_default_product_weight():
    """Test default product weight being 20."""
    prod = Product("Test Product")
    assert prod.weight == 20


def test_stealability():
    """Test stealability method for product class"""
    prod = Product("Test Product")
    assert prod.stealability() == "Kinda stealable."


def test_explode():
    """Test explode method for product class"""
    prod = Product("Test Product")
    assert prod.explode() == "...boom!"


def test_boxing_glove():
    """Test child class methods"""
    test_1 = BoxingGlove("Punchy the Third")
    test_2 = BoxingGlove("Test Boxing Glove", price=10, weight=45,
                         flammability=0)
    assert "very" in test_1.stealability().lower()
    assert "hurt" in test_1.punch().lower()
    assert "glove" in test_1.explode().lower()
    assert "not" in test_2.stealability().lower()
    assert "ouch" in test_2.punch().lower()


def test_product_methods():
    """Test parent class methods"""
    test_1 = Product("A Cool Toy")
    test_2 = Product("Test Toy", price=20, weight=100,
                     flammability=2)
    test_3 = Product("Another Test Toy", price=20,
                     weight=100, flammability=2)
    assert "kinda" in test_1.stealability().lower()
    assert "not" in test_2.stealability().lower()
    assert "BABOOM" in test_2.explode()


def test_default_num_products():
    """Test default size of products list"""
    prod_lst = generate_products()
    assert len(prod_lst) == 30


def test_legal_names():
    """Test generated name validity of product batch"""
    prod_lst = generate_products()
    for prod in prod_lst:
        names = prod.name.split()
        assert names[0] in ADJECTIVES
        assert names[1] in NOUNS


def test_generate_products_product_method():
    """Test product methods on generated products"""
    products = generate_products()
    for prod in products:
        assert 2.5 >= prod.flammability >= 0.0
        assert 100 >= prod.price >= 5
        assert isinstance(prod.price, int)
        assert 100 >= prod.weight >= 5
        assert 101 >= 100
