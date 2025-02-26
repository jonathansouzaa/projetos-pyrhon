import os

usuario = []

def exibir_opcoes():
    print('(1) Login')
    print('(2) Cadastro usuario')
    print('(3) Exibir cadastros')
    print('(4) Desabilitar aplicativos do windows inicializados com o sistema')
    print('(5) Sair\n')
    
def inicio_main():
    print('\n')
    input('escreva qualquer tecla para voltar ao menu ')       
    main()

def escolher_opc():
    try:
        opc = int(input('Escolha uma opção: '))    
        if opc == 1:
            print('Bem vindo ao login\n')
        elif opc == 2:
            print('Bem vindo ao Cadastro\n')
            cadastrar_usuario()
        elif opc == 3:
            print('Exibir usuarios\n')
            os.system('cls')
            exibir_usuarios_cadastrados()
        elif opc == 4:
            print('Desabilitar apps em segundo\n')
            os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f')
            inicio_main()
        elif opc == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def opcao_invalida():
    print('Opção invalida.')
    inicio_main()

def finalizar_app(): 
    os.system('cls')
    print('Encerrar app')

def cadastrar_usuario():
    print(' Cadastrar Usuário\n')
    inserir_usuario = input('Escreva o nome do usuário: ')
    usuario.append(inserir_usuario)
    print(f'O usuario {inserir_usuario} foi cadastrado com sucesso')
    opc = input('Deseja realizar um novo cadastro ? (y) para sim e qualquer tecla para sair: ')
    if opc == 'y':
        os.system('cls')
        cadastrar_usuario()
    else:
        main()

def exibir_usuarios_cadastrados():
    for usuarios in usuario:
        print(f'Usuario: {usuarios}') 
    inicio_main()   

def main():
    os.system('cls')
    exibir_opcoes()
    escolher_opc()

if __name__ =='__main__':
    main()
