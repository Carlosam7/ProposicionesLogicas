from typing import Optional

class Node:
  def __init__ (self, proposition: 'str') -> None:
    self.__proposition = proposition #Proposición que contiene el nodo
    self.__left: Optional['Node'] = None
    self.__right: Optional['Node'] = None

  def get_proposition(self):
    return self.__proposition

  def set_proposition(self, proposition):
    self.__proposition = proposition

  def get_left(self):
    return self.__left

  def set_left(self, left):
    self.__left = Node(left)

  def get_right(self):
    return self.__right

  def set_right(self, right):
    self.__right = Node(right)