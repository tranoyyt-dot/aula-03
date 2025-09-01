senha = input('Digite a senha do seu cartão de credito para continuar [;)   :')
cllt = 0
while cllt < 3:
    cllt += 1
    tentativa = input('Digite a senha para a tentativa de saque:')
    if tentativa != senha:
        print('Senha incorreta')
        continue
    else:
        print('Senha correta - executando saque...')
        break