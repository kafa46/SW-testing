'''Shopping Cart Test 1
    - Purpose: Test Requirement 1 (add functionality)
    - Description: Test whether when one item is added into shopping cart,
        the number of item in cart is increased by 1.
'''

from cart import Cart

def test_add_function():
    '''Test adding one item into empty shopping cart'''
    cart = Cart(max_number= 5)
    cart.add('apple')
    assert cart.get_number_of_items() == 1
