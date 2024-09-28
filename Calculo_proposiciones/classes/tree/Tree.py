from classes.node.Node import Node
from typing import List

class Tree:
  def __init__(self, root: 'Node') -> None:
    self.__root = root

  def get_root(self) -> 'Node':
    return self.__root #Proposicion original

  '''Recorridos del arbol'''
  def preorder_nr(self) -> None:
    p, s = self.__root, []
    while p is not None or len(s) != 0:
      if p is not None:
        print(p.get_proposition())
        s.append(p)
        p = p.get_left()
      else:
        p = s.pop()
        p = p.get_right()

  def postorder_nr(self) -> List:
    p, s, s_data = self.get_root(), [], []
    lista = []
    s.append(p)
    while len(s) != 0:
      p = s.pop()
      s_data.append(p.get_proposition())
      if p.get_left() is not None:
          s.append(p.get_left())
      if p.get_right() is not None:
          s.append(p.get_right())

    while len(s_data) != 0:
      lista.append(s_data.pop())
    return lista


  def levels_nr(self) -> List:
    p, q = self.get_root(), []
    lista = []
    q.append(p)
    while len(q) != 0:
      p = q.pop(0)
      if p.get_proposition() not in lista:
        lista.append(p.get_proposition())
      if p.get_left() is not None:
          q.append(p.get_left())
      if p.get_right() is not None:
          q.append(p.get_right())
    return lista[::-1]