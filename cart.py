'''Source code for shpping cart implementation.
Author: Giseop Noh
Created: 2022. xx. xx
'''

from typing import Dict, List

class Cart:
    '''Class for shopping cart'''

    def __init__(self, max_number: int, price_table: Dict) -> None:
        self.items: List[str] = []
        self.max_number = max_number
        self.price_table = price_table

    def add(self, item:str) -> None:
        '''add one item into shopping cart'''
        self.items.append(item)

    def get_number_of_items(self) -> int:
        '''get the number of items in shopping cart'''
        return len(self.items)

    def get_items(self,) -> List[str]:
        '''get all items from shopping cart'''
        return self.items

    def get_total_price(self, ) -> int:
        '''get total price of all items
        in the shopping cart
        '''

        total_price = 0

        # for item in self.items:
        #     total_price += self.price_table.get(item)
        # return total_price

        return sum([total_price + self.price_table[item] for item in self.items])


if __name__=='__main__':

    # An Example of Manual Test
    
    price_table = {
        'apple': 300,
        'orange': 200,
        'strawberry': 500,
    }

    cart = Cart(max_number=5, price_table=price_table)
    cart.add('apple')
    cart.add('orange')
    cart.add('orange')
    
    print(f'Items in cart: {cart.get_items()}')
    print(f'Number of items: {cart.get_number_of_items()}')
    print(f'Total price: {cart.get_total_price()}' )
