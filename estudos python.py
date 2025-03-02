import os
import subprocess
usuario = [{'nome':'', 'email':'', 'telefone':''}]

def exibir_opcoes():
    print('(1) Limpar arquivos inutes windows')
    print('(2) instalar programas')
    print('(3) Configurar maximo desempenho')
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
            print('limpar arquivos inuteis windows\n')
            executar_comando = 'Remove-Item -Path C:\\Windows\\Temp\\* -Recurse -Force; New-Item -Path C:\\Windows\\Temp -ItemType Directory -Force;Remove-Item -Path $env:TEMP\\* -Recurse -Force; New-Item -Path $env:TEMP -ItemType Directory -Force'''
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
    try:
        nome_usuario = input('Digite o nome do usuário: ')
        email_usuario = input('Digite o email do usuário: ')
        telefone_usuario = input('Digite o telefone do usuário: ')
        dados_usuario = {'nome':nome_usuario, 'email':email_usuario, 'telefone':telefone_usuario}
        usuario.append(dados_usuario)
        print(f'O usuario {nome_usuario} foi cadastrado com sucesso')
        opc = input('Deseja realizar um novo cadastro ? (y) para sim e qualquer tecla para sair: ')
        if opc == 'y':
            os.system('cls')
            cadastrar_usuario()
        else:
            main()
    except:
        print('Erro ao cadastrar usuário')
        inicio_main()

def exibir_usuarios_cadastrados():
    for usuarios in usuario:
        nome_usuario = usuarios['nome']
        email_usuario = usuarios['email']
        telefone_usuario = usuarios['telefone']
        print(f'Usuario: {nome_usuario} Email: {email_usuario} Telefone: {telefone_usuario}') 
    inicio_main()   

def main():
    os.system('cls')
    exibir_opcoes()
    escolher_opc()

if __name__ =='__main__':
    main()
