from trilha import Trilha
from pessoa import Pessoa
from pessoa import Amigos
from pessoa import Familia
from pessoa import Guia

'''
Pontuacao:
1 Amigo: +15
1 Membro da família: + 20 pts
1 guia: -5 pts
1 pessoa menor de idade: + 10 pts
Mais de 10 pessoas na trilha: -5 pts
'''


amigo1 = Amigos(' ', 0, ' ') #nome, idade, endereco
familia1 = Familia(' ', 0, ' ') #nome, idade, endereco
trilha1 = Trilha('', 0, ' ', ' ')
guia1 = Guia('', 0, 'a', 0.0) #nome, idade, endereço, valor médio por trilha 


# tem_guia = False

pontuacao_total = 0

def cadastraTrilha(): 
    print('-- Cadastro de trilha: \n')
    trilha1.distancia_total = float(input('Digite a distância total da trilha em km: '))
    trilha1.grau_dificuldade = input('Digite o grau de dificuldade da trilha (fácil, médio, difícil): ')
    trilha1.localizacao = input('Digite a localização da trilha: ')
    trilha1.nome = input('Dê um nome a sua trilha: \n')
    input('Aperte ENTER para começar a cadastrar as pessoas que foram à trilha com você!')
    
    qtd_pessoas = int(input('Quantas pessoas você deseja cadastrar?\n'))
    
    cont = 1

    qtd_pessoas = 0

    while cont <= qtd_pessoas:
        print(f'\n -- Cadastro da  {cont}° pessoa: \n')
        cadastraPessoa() 
        cont += 1

    print('Cadastro concluído com sucesso!')

def cadastraPessoa ():
    # global qtd_pessoas #torna a variável global
    global pontuacao_total


    tipo_pessoa = input('Digite "amigo" se a pessoa cadastrada for seu amigo, "família" se a \npessoa for um membro da sua família, ou "guia" se a pessoa for um guia: \n')
    
    if tipo_pessoa == 'amigo':
        print('\n- Cadastrando amigo: \n')
        amigo1.nome = input('1. Nome: ')
        amigo1.idade = int(input('2. Idade: '))
        amigo1.endereco = input('3. Endereço: ')

        qtd_pessoas += 1 # Adiciona o amigo cadastrado à quantidade total de pessoas

        #pontuação
        pontuacao_total += 15 #Motivo: +1 amigo
        
        if amigo1.idade < 18:
            pontuacao_total += 10

        print('Amigo cadastrado com sucesso!\n')


    elif tipo_pessoa == 'familia':
        qtd_pessoas += 1
        print('\nCadastro de membro da família: \n')
        familia1.nome = input('1. Nome: ')
        familia1.idade = int(input('2. Idade: '))
        familia1.endereco = input('3. Endereço: ')


        #pontuação
        pontuacao_total += 20 # Motivo: +1 membro da família

        if familia1.idade < 18:
            pontuacao_total += 10

        print('Membro da família cadastrado com sucesso!\n')


    elif tipo_pessoa == 'guia':
        print('\nCadastro de guia: \n')
        guia1.nome = input('1. Nome: ')
        guia1.idade = int(input('2. Idade: '))
        guia1.endereco = input('3. Endereço: ')


        #pontuação
        pontuacao_total -= 5  #Motivo: +1 guia

        if guia1.idade < 18:
            pontuacao_total += 10

        print('Guia cadastrado com sucesso!\n')

    else: 
        raise ValueError('Informação inválida!')


    if qtd_pessoas == 11: #Se a condição do if fosse ser maior que 10, a cada pessoa adicionada a partir da 10° resultaria em uma perda de 5 pontos. Já que só é cadastrada uma pessoa por vez, quando o n° passar de 10, haverá a perda dos pontos 
        pontuacao_total -= 5


def mostraPontuacao():
    print('---------------------------------------')
    print('|         Pontuação Total             |')
    print(f'|              {pontuacao_total} pts                 |')
    print('--------------------------------------- \n')



# Decoração
print ('\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print ('----------------- Bem vindo ao My Log Tracks ---------------------------')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
input('Aperte ENTER para cadastrar uma nova trilha')
cadastraTrilha()
mostraPontuacao()