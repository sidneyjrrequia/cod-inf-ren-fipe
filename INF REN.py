# INFORMATIVO RENOVAÇÃO AUTO, MOTO, RESIDENCIAL.
if __name__ == '__main__':

    insurance = input('Carro(C), Moto(M) ou Residencial(R)?: ')

    time = input('Período manhã (M) ou tarde (T)?: ')

    if time == 'M':
        time = 'bom dia'
    elif time == 'T':
        time = 'boa tarde'

    item = input('Carro / Moto / Endereço: ')
    name = input('Nome: ')
    day = input('Dia: ')
    month = '05'
    # promo = input('Promoção dd/mm: ')
    promo = '01/05'
    person = 'Sidney Requia'
    print('\n')

    if insurance == 'C':

        print(f'👤 *Muito {time} Sr(a). {name}!*\n'
              '\n'

              f'🚘 *O seguro do seu veículo {item} está vencendo em {day}/{month}.*\n'
              f'Gostaria de te tranquilizar, pois já estamos vendo a melhor opção e com antecedência estaremos '
              f'ligando para lhe passar a melhor proposta. 😃\n'
              '\n'

              f'❕*Novidades*\n'
              f'- Redução significativa nas taxas para pagamento no cartão de crédito!\n'
              f'- Parcelamento em até 10x sem juros no cartão de crédito.\n'
              '\n'

              f'‼️ *SuperCombo* ‼️\n'
              f'✅ Exclusividades: \n'
              f'- *Franquia inteiramente GRÁTIS em caso de sinistro*;\n'
              f'- Aumento de coberturas;\n'
              f'- Aumento de carro reserva\n'
              f'- Ao contratar o seguro do seu carro você leva um seguro residencial;\n'
              f'- 🏡 Super assistência residencial Porto Seguro (reparos hidráulicos e elétricos, conserto '
              f'de geladeira, fogão, maquinas de lavar, etc);\n'
              f'- Desentupimento;\n'
              f'- Conserto de ar condicionado;\n'
              '\n'

              f'📱 Ligaremos antes do vencimento com os preços já calculados e, com absoluta certeza, com um *super '
              f'desconto* que vai lhe deixar bem contente. 😁😁😁\n'
              '\n'

              f'Me chamo {person}\n'
              f'Meu telefone é *4007-2555* ☎️\n'
              f'Um super abraço, conte sempre comigo! 😊\n'

              f'\n*A partir do dia {promo} teremos um desconto especial que será aplicado, peço que aguarde para '
              f'ser disponibilizado o melhor preço para seu seguro, desde já agradeço a paciência!* 😉\n'

              f'\n*Veja a mensagem que o proprietário, Luiz Cerbino Neto, deixou para você no vídeo a seguir!*\n'


              f'\nTipo: {insurance}'
              f'\nPeríodo: {time}'
              f'\nNome: {name}'
              f'\nVeículo: {item}'
              f'\nVencimento: {day}/{month}'
              f'\nOperador: {person}'
              f'\nDia da promoção: {promo}')

    elif insurance == 'R':

        print(f'👤 *Muito {time} Sr(a). {name}!*\n'
              '\n'

              f'🏠 *O seu seguro residencial do local {item} está vencendo em {day}/{month}.*\n'
              f'Gostaria de te tranquilizar, pois já estamos vendo a melhor opção e com antecedência estaremos '
              f'ligando para lhe passar a melhor proposta. 😃\n'
              '\n'

              f'❕*Novidades*\n'
              f'- Redução significativa nas taxas para pagamento no cartão de crédito!\n'
              f'- Parcelamento em até 10x sem juros no cartão de crédito.\n'
              '\n'

              f'📱 Ligaremos antes do vencimento com os preços já calculados e, com absoluta certeza, com um *super '
              f'desconto* que vai lhe deixar bem contente. 😁😁😁\n'
              '\n'

              f'Me chamo {person}\n'
              f'Meu telefone é *4007-2555* ☎️\n'
              f'Um super abraço, conte sempre comigo! 😊\n'

              f'\n*A partir do dia {promo} teremos um desconto especial que será aplicado, peço que aguarde '
              f'para ser disponibilizado o melhor preço para seu seguro, desde já agradeço a paciência!* 😉\n'


              f'\nTipo: {insurance}'
              f'\nPeríodo: {time}'
              f'\nNome: {name}'
              f'\nVeículo / local: {item}'
              f'\nVencimento: {day}/{month}'
              f'\nOperador: {person}'
              f'\nDia da promoção: {promo}')

    elif insurance == 'M':

        print(f'👤 *Muito {time} Sr(a). {name}!*\n'
              '\n'

              f'🏍 *O seguro do seu veículo {item} está vencendo em {day}/{month}.*\n'
              f'Gostaria de te tranquilizar, pois já estamos vendo a melhor opção e com antecedência estaremos '
              f'ligando para lhe passar a melhor proposta. 😃\n'
              '\n'

              f'❕*Novidades*\n'
              f'- Redução significativa nas taxas para pagamento no cartão de crédito!\n'
              f'- Parcelamento em até 10x sem juros no cartão de crédito.\n'
              '\n'

              f'📱 Ligaremos antes do vencimento com os preços já calculados e, com absoluta certeza, com um *super '
              f'desconto* que vai lhe deixar bem contente. 😁😁😁\n'
              '\n'

              f'Me chamo {person}\n'
              f'Meu telefone é *4007-2555* ☎️\n'
              f'Um super abraço, conte sempre comigo! 😊\n'

              f'\n*A partir do dia {promo} teremos um desconto especial que será aplicado, peço que aguarde '
              f'para ser disponibilizado o melhor preço para seu seguro, desde já agradeço a paciência!* 😉\n'


              f'\nTipo: {insurance}'
              f'\nPeríodo: {time}'
              f'\nNome: {name}'
              f'\nVeículo / local: {item}'
              f'\nVencimento: {day}/{month}'
              f'\nOperador: {person}'
              f'\nDia da promoção: {promo}')