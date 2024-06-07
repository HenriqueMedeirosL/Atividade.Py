# Exemplo de código para tratamento de erros em python

try:
  a = int(input('Digite um numerador: ')) # Digtando um numerador
  b = int(input('Digite um denominador: ')) # Digitando um denominador
  res = a / b

except ZeroDivisionError:
  print('Não é permitido divisão por zero!')
except KeyboardInterrupt:
  print('\nO usuário optou por não informar nada...')
except (ValueError, NameError):
  print('Digite um número inteiro: ')
except Exception as erro:
  print(f'Ocorreu um erro: {erro.__class__}')
else:
  print(f'O resultado de {a}/{b} é {res}')
finally:
  print('A prática leva a perfeição. \nContinue assim \o/')