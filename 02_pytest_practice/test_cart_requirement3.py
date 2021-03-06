'''Shopping Cart Test 3
    - Purpose: Test Requirement 3 ('max_number' limit in shopping cart)
    - Description: Test whether when user add more than max limit into the cart,
        the system must stop or throw errors properly.
'''

import random
from cart import Cart

p_table = {
    'apple': 300,
    'orange': 200,
    'strawberry': 500,
}

def test_max_number_limit():
    '''Test the max number of allowed items into shopping cart'''

    cart = Cart(max_number= 5)

    for _ in range(cart.max_number):
        item_choice = random.choice(list(p_table.keys()))
        cart.add(item_choice)

    cart.add('apple')
