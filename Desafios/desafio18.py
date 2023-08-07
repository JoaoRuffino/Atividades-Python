from math import sin, cos, tan, radians
ang = float(input('Insira um ângulo qualquer: '))

sen1 = sin(radians(ang))
cos1 = cos(radians(ang))
tan1 = tan(radians(ang))
print('O seno do ângulo {} é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(ang, sen1, cos1, tan1))
