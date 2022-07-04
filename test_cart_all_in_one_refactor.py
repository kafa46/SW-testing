'''Shopping Cart Test
    - Purpose: Test Requirements 1 ('add' functionality)
    - Description: Test whether when one item is added into shopping cart,
        the number of item in cart is increased by 1.
    - Requirements:
        1. One can add an item(s) into the cart.
        2. One can check the total number of items from the cart.
        3. There exists the maximum limit of items to the cart.
        4. One can verify the total cost of items in the cart.
'''

import random
import pytest
from cart import Cart


# Price table for available item in the cart.
p_table = {
    'apple': 300,
    'orange': 200,
    'strawberry': 500,
}

@pytest.fixture
def cart():
    '''pytest fixture function'''
    return Cart(max_number=5)

def test_add_function(cart):
    '''Test: Requirement I ('add' functionality)
    Test whether when one item is added into shopping cart,
    the number of item in cart is increased by 1.
    '''
    
    cart.add('apple')
    assert cart.get_number_of_items() == 1


def test_get_number_of_items_from_cart(cart):
    '''Test adding one item into empty shopping cart'''
    
    test_number = 3

    for _ in range(test_number):
        item_choice = random.choice(list(p_table.keys()))
        cart.add(item_choice)

    print(f'\nTest>>> Added item: {cart.items}')
    print(f'Test>>> The Number of added items: {len(cart.items)}')

    assert cart.get_number_of_items() == test_number


def test_max_number_limit(cart):
    '''Test the max number of allowed items into shopping cart'''

    for _ in range(cart.max_number):
        item_choice = random.choice(list(p_table.keys()))
        cart.add(item_choice)

    # cart.add('apple')


def test_get_total_price(cart):
    '''Test total cost returned'''

    cart.add('apple')
    cart.add('orange')
    assert cart.get_total_price(p_table) == 500
