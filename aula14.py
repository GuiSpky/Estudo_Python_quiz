# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
conta_acerto = 0
conta_erro = 0
for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    
    for i,opcao in enumerate(opcoes):
        print(f'{i})',opcao)

    escolha = input('escolha uma Opção: ')
    print()

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    os.system('clear')

    if acertou:
        print('Acertou 👍')
        print()
        conta_acerto += 1
    else:
        print('Errou ❌')
        print()
        conta_erro += 1
        
print()
print(f'Você acertou {conta_acerto} perguntas')
print(f'E errou {conta_erro}')
print()
