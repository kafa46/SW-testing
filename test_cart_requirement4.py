'''Shopping Cart Test 4
    - Purpose: Test Requirement 4 ('total cost' limit in shopping cart)
    - Description: Test whether one can extract total price of
                    all items in the cart.
'''

from cart import Cart

p_table = {
    'apple': 300,
    'orange': 200,
    'strawberry': 500,
}

def test_get_total_price():
    '''Test total cost returned'''

    cart = Cart(max_number= 5)
    cart.add('apple')
    cart.add('orange')
    assert cart.get_total_price(price_table=p_table) == 500
