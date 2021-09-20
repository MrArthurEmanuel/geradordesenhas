import random, string, os
import time
print('#' *49)
print('### Gerador de Senhas ABSURDAMENTES FORTES!!! ###')
print('#' *49)
print('\nBy. Mr.Arthur (EU MESMO)')

tamanho = int(input('\nDigite o tamanho da senha desejada: '))


if tamanho < 8:
    conf = str(input('Senha fraca. Minimo recomendado: 8 Digitos. Deseja continuar mesmo assim? Se sim, digite "y": '))

    if conf == 'y':
        chars = string.ascii_letters + string.digits + '!@#$%&*ç'
        rnd = random.SystemRandom()

        print('\nSua senha é: ')
        print('↓' * 30)
        print(''.join(rnd.choice(chars) for i in range(tamanho)))
        print('')

        time.sleep(3)
        os.system('pause')
    else:
        tamanho = int(input('\nDigite o tamanho da senha desejada: '))
        chars = string.ascii_letters + string.digits + '!@#$%&*ç'
        rnd = random.SystemRandom()

        print('\nSua senha é: ')
        print('↓' * 30)
        print(''.join(rnd.choice(chars) for i in range(tamanho)))
        print('')
        time.sleep(3)
        os.system('pause')
else:
    chars = string.ascii_letters + string.digits + '!@#$%&*ç'
    rnd = random.SystemRandom()

    print('\nSua senha é: ')
    print('↓' * 30)
    print(''.join(rnd.choice(chars) for i in range(tamanho)))
    print('')

    time.sleep(3)
    os.system('pause')