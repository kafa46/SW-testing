'''Shopping Cart Test 2
    - Purpose: Test Requirement 2 ('get_number_of_items' functionality)
    - Description: Test whether when ask the number of items to cart,
        the number of item in the cart is returned correctly.
'''

import random
from cart import Cart

PRICE_TABLE = {
    'apple': 300,
    'orange': 200,
    'strawberry': 500,
}


def test_get_number_of_items_from_cart():
    '''Test adding one item into empty shopping cart'''
    cart = Cart(max_number= 5, price_table=PRICE_TABLE)
    test_number = 3

    for _ in range(test_number):
        item_choice = random.choice(list(cart.price_table.keys()))
        cart.add(item_choice)

    print(f'\nTest>>> Added item: {cart.items}')
    print(f'Test>>> The Number of added items: {len(cart.items)}')

    assert cart.get_number_of_items() == test_number
