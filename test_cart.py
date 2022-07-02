from cart import Cart

# 카트에 상품 1개를 담았을 경우
# 카트에 담긴 상품 수량이 1개 증가하는지 테스트
def test_add_function():
    '''test adding one item into empty shopping cart'''
    cart = Cart(5)
    cart.add('apple')
    assert cart.get_number_of_items() == 1


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
