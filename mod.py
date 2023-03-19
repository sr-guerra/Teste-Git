a = input('Digite um número ímpar:')
r = int(a) % 2

if r == 1:
    print(f'Muito bem, está correto, o número {a} é ímpar. Agora digite um númeto par.')

    aa = input('Digite um número par:')
    rr = int(aa) % 2

    if rr == 0:
        print(f'Muito bem! teste concluído com sucesso. O número {aa} é par.')
    else:
        print(f'Que pena! Você falhou no teste. O número {aa} é ímpar.')

else:
    print(f'Que pena! Você falhou no teste. O número {a} é par.')