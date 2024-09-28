# -*- coding: utf-8 -*-
"""Arango_Carlos_Monserrat_Ándres_Laboratotio2.ipynb

Original file is located at
    https://colab.research.google.com/drive/1LSh8SjFNVWkTsiIRh1QtoeJITifUdzv1
"""

#Las proposiciones deben ir encerradas entre paréntesis. Ejemplo: (p -> q)

from controllers.truth_value import truth_value


if truth_value('((p -> q) & (q -> p))', '(p <-> q)'):
  print('Las proposiciones son equivalentes.')
else:
  print('Las proposiciones NO son equivalentes.')