from product import *


class TestProduct:
    def test_initialize_product(self):
        product = Product(1, 2)
        assert product.days_remaining == 1
        assert product.quality == 2

    def test_tick_fresh(self):
        # Quality for a fresh product is decreased by 1
        product = Product(2, 3)
        product.tick()
        assert product.days_remaining == 1
        assert product.quality == 2

    def test_tick_past_due(self):
        # Quality for a product past due is decreased by 2
        product = Product(0, 3)
        product.tick()
        assert product.days_remaining == -1
        assert product.quality == 1

    def test_tick_rotten(self):
        # Quality for a rotten product remains 0
        product = Product(0, 0)
        product.tick()
        assert product.days_remaining == -1
        assert product.quality == 0
