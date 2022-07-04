from trilha import Trilha
from pessoa import Pessoa
from pessoa import Amigos
from pessoa import Familia
from pessoa import Guia



amigo1 = Amigos(' ', 0, ' ') #nome, idade, endereco
familia1 = Familia(' ', 0, ' ') #nome, idade, endereco
trilha1 = Trilha('', 0, ' ', ' ')
trilha2 = Trilha(0, 0, ' ', ' ')
guia1 = Guia('', 0, 'a', 0.0) #nome, idade, endereço, valor médio por trilha    


tem_guia = False
qtd_pessoas = 0
pontuacao = 0

def cadastraPessoa ():
    print('\n -- Cadastro de pessoa: \n')
    global tem_guia
    global qtd_pessoas
    global pontuacao
    
    tipo_pessoa = input('1. Digite "amigo" se a pessoa cadastrada for seu amigo, "família" se a \npessoa for um membro da sua família, ou "guia" se a pessoa for um guia: \n')
    
    if tipo_pessoa == 'amigo':
        qtd_pessoas += 1
        print('\n- Cadastrando amigo: \n')
        # amigo1.nome = input('Digite o nome do amigo: ')
    

    elif tipo_pessoa == 'familia':
        qtd_pessoas += 1
        print('\nCadastro de membro da família: \n')


    elif tipo_pessoa == 'guia':
        qtd_pessoas += 1
        tem_guia = True


# Decoração
print ('\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print ('----------------- Bem vindo ao My Log Tracks ---------------------------')

cadastraPessoa()