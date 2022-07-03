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
from cart import Cart

# Price table for available item in the cart.
PRICE_TABLE = {
    'apple': 300,
    'orange': 200,
    'strawberry': 500,
}


def test_add_function():
    '''Test: Requirement I ('add' functionality)
    Test whether when one item is added into shopping cart,
    the number of item in cart is increased by 1.
    '''

    cart = Cart(max_number= 5, price_table=PRICE_TABLE)
    cart.add('apple')
    assert cart.get_number_of_items() == 1


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


# 카트에 있는 상품 중에서
# 원하는 상품이 있는지 확인하는 테스트
def test_added_item_in_cart():
    '''test checking to see an existing item'''
    cart = Cart(5)
    cart.add('apple')
    assert 'apple' in cart.get_items()

# 카트에 최대 허용 가능한 상품 수량을
# 확인하는 테스트
def test_check_max_number_in_cart():
    '''checking the max number is working'''
    cart = Cart(5) # 최대 5개
    for _ in range(6):
        cart.add('noodle')
