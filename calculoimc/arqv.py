import math
import os
from time import sleep


def imc():
  altura= float(input('Digite a altura em metros: '))
  peso = float(input('Digite o seu peso: '))
  fimc = peso / (math.pow(altura, 2))
  print('A Calcular')
  sleep(1.9) #temporizador
  os.system('cls') #limpar tela
  print('O seu Índice de massa corporal é de {:.2f}.'. format(fimc))
  if fimc < 17:
   print('Muito abaixo do peso')
  elif fimc >= 17 and  fimc <=18.49:
   print('Abaixo do peso')
  elif fimc >= 18.50 and  fimc <=24.99:
    print('Peso normal')
  elif fimc >= 25 and  fimc <=29.99:
    print('Acima do peso')
  elif fimc >= 30 and  fimc <=34.99:
    print('Obesidade I')
  elif fimc >= 35 and  fimc <=39.99:
    print('Obesidade II (severa)')
  else:
     print('Obesidade III (mórbida)')

imc()