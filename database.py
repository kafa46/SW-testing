from dataclasses import dataclass



@dataclass
class ItemDatabase:
    '''Item database class for mocking'''

    database = {}

    def get(self, item: str) -> int:
        '''get method for cart.py'''
        pass
