from classes.node.Node import Node
from classes.tree.Tree import Tree
from controllers.split_proposition import split_proposition

def build_tree(proposition: 'str') -> 'Tree':
  proposition = proposition.replace(' ', '') #Se eliminan los espacios
  tree = Tree(Node(proposition))  # Crear un árbol con la proposición completa
  s = [tree.get_root()]
  while s:
    p = s.pop()
    left, operator, right = split_proposition(p.get_proposition())
    if operator:
      #Se divide la proposición y se guardan las partes en un nodo left y right
      if left:
        p.set_left(left)
        s.append(p.get_left())
      if right:
        p.set_right(right)
        s.append(p.get_right())
    else:
      pass
      #print('Proposición básica.')
  return tree