'''import math'''
from math import radians, sin, cos, tan
ang = float(input('Digite o angulo que deseja:'))
sen = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {} tem a COSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))