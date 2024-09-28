from controllers.find_operator import find_operator

def split_proposition(prop:'str') -> 'tuple':
  """Esta función divide la proposición en sus componentes sin operadores"""
  if prop.startswith('(') and prop.endswith(')'):
    prop = prop[1:-1]

  index, operator = find_operator(prop)
  #print(operator)
  if index == -1:
    # No se encontró operador
    return prop, None, None

  left = prop[:index]
  if operator == '->':
    right = prop[index+2:]
  elif operator == '<->':
    right = prop[index+3:]
  else:
    right = prop[index+1:]
  return left, operator, right