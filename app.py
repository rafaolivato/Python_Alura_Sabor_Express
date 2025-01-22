import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
{'nome':'Pizza Suprema', 'categoria': 'Italiano', 'ativo': True},
{'nome':'Casa do Pão de Queijo', 'categoria': 'Cafeteria', 'ativo': False}
]

def exibir_nome_do_programa():
    

    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')



def exibir_opcoes():
    print('Escolha uma opção: ')
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar status do Restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) )
    print(linha)
    print(texto)
    print(linha)
    print()


def finalizar_app():
    exibir_subtitulo('Finalizando aplicação...')

def voltar_ao_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal.')
    main()

def cadastrar_novo_restaurante():
    '''Função para cadastrar um novo restaurante
    
    input: nome do restaurante, categoria do restaurante

    output: mensagem de sucesso

    '''
    exibir_subtitulo('Cadastrar novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
   
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')


    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar Restaurantes\n')
    
    print('Nome'.ljust(32), '| Categoria'.ljust(32), ' | Status')
    print('-' * 90)
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(30)} |  {categoria.ljust(30)} | {ativo}')
   
    voltar_ao_menu_principal()

def alternar_status_restaurante():
    exibir_subtitulo('Alternar status do restaurante\n')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()   
    


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
        main()