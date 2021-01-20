
'''
class abc.ABC
A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from ABC avoiding sometimes confusing metaclass usage, for example:

from abc import ABC

class MyABC(ABC):
    pass
## Abstract Classes in Python .....
    '''
# hackerank implementation code
'''
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass
'''
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price = price
    @classmethod
    def display(self):
        print('Title:',title)
        print('Author:',author)
        print('Price:',price)

'''
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
'''
