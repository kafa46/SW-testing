'''Source code for shpping cart implementation.
Author: Giseop Noh
Affiliation: Cheongju University, South Korea
License: MIT (see LICENSE file in current directory)

This simple code is an implematation of shopping cart app
for the practice of 'Pytest'.

The shopping cart has five requirements as follows:
    - Requirements:
        1. One can add an item(s) into the cart.
        2. One can check the total number of items from the cart.
        3. There exists the maximum limit of items to the cart.
        4. One can verify the total cost of items in the cart.
'''

from typing import Dict, List

class Cart:
    '''Class for shopping cart'''

    def __init__(self, max_number: int, price_table: Dict) -> None:
        self.items: List[str] = []
        self.max_number = max_number
        self.price_table = price_table


    def add(self, item:str) -> None:
        '''Add one item into empty shopping cart'''
        if self.get_number_of_items() >= self.max_number:
            raise OverflowError(f'Cannot add more than max_size {self.max_number}')
        self.items.append(item)


    def get_number_of_items(self,) -> int:
        '''Get the number of items in shopping cart'''
        return len(self.items)


    def get_total_price(self, ) -> int:
        '''Get total price of all items
        in the shopping cart
        '''

        total_price = 0
        # for item in self.items:
        #     total_price += self.price_table.get(item)
        # return total_price

        return sum([total_price + self.price_table[item] for item in self.items])


if __name__=='__main__':

    # An Example of Manual Test

    p_table = {
        'apple': 300,
        'orange': 200,
        'strawberry': 500,
    }

    cart = Cart(max_number=5, price_table=p_table)
    cart.add('apple')
    cart.add('orange')
    cart.add('orange')

    print(f'Number of items: {cart.get_number_of_items()}')
    print(f'Total price: {cart.get_total_price()}' )
