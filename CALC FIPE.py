# CÁLCULO COMPARAÇÃO FIPE ANO ANTERIOR X ATUAL.
def calc(old_v, new_v):
    new = (new_v - old_v) / old_v

    if new < 0.12:
        print(f'🚘 *Mundo automotivo 🏍 :*\n'
              '\n'

              f'*O seu veículo teve uma valorização de {"%.1f" % (new * 100)}%!*\n'
              '\n'

              f'⚠️Isso vai impactar um pouquinho no valor do seu seguro, mas pode ficar tranquilo(a), '
              f'*farei o máximo para conseguir o melhor preço!*\n')
    else:
        print(f'🚘 *Mundo automotivo 🏍 :*\n'
              '\n'

              f'*O seu veículo teve uma valorização de {"%.1f" % (new * 100)}%!*\n'
              '\n'

              f'⚠️Valorizou muito, isso vai impactar um pouquinho no valor do seu seguro, mas pode ficar tranquilo(a), '
              f'*farei o máximo para conseguir o melhor preço!*\n')

    print(f'Valorização de R${new_v - old_v}')


if __name__ == '__main__':
    old_value = int(input('Digite o valor do veículo no ano passado: '))
    new_value = int(input('Digite o valor do veículo nesse ano     : '))

    print('\n')

    calc(old_value, new_value)