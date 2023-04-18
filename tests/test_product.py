from product_samples import *
import pytest

@pytest.mark.skip()
def test_population():
    product1.populate_product_using_link(product1.link_to_product,product1.image_link)
