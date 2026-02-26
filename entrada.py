'''
Programa para entraada de dadoa de alunos de 
universidade para geração de email e senha automático
'''


while True:

    nome=input('Olá, digite o seu nome, por favor:\n').strip()
    sobrenome=input('Digite o seu sobrenome:\n').strip()
    dia=int(input('Qual o dia do seu nascimento?\n').strip())
    mes=(input('Qual o mês do seu nascimento?\n').strip())
    ano=int(input('Qual o ano do seu nascimento?\n').strip())
    universidade=input('Digite o nome da sua universidade:\n').strip()

    print('\nSuas informações são as seguinte:{} {},{}/{}/{},{}\n'.format(nome.upper(),sobrenome.upper(),dia,mes,ano,universidade.upper()))

    verificar=input('\nAs informações, estão corretas?\n').strip().lower()
    if verificar in ['s','sim']:
     print('\nEstamos gerando o seu email e senha\n')
     break
    elif verificar in ['n', 'nao', 'não']:
     print('\nOk, vamos tentar novamente!\n')

    else:
     print('\nResposta inválida! Digite apenas: (s) ou (n) \n')

email= nome.lower()+'.'+sobrenome.lower()+'@'+universidade.lower()+'.br'

forms= email
letraA= forms.count('a')
letraE= forms.count('e')
letraI= forms.count('i')
letraO= forms.count('o')
letraU= forms.count('u')

senha= 'u'+str(letraA) +'i'+str(letraE) +'v'+str(letraI)+'e'+str(letraO)+'r'+str(letraU)

print('\nO seu email é: {}'.format(email))
print('A sua senha é: {}\n'.format(senha))
