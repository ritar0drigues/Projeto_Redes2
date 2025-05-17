import os
import subprocess

def gerar_compose():
    print("\nGerando o arquivo docker-compose.yml...")
    os.system("cd gera_yml && pip install --quiet -r requirements.txt")
    os.system("cd gera_yml && python gerar_yaml.py")
    os.system("cd gera_yml && python docker_compose_create.py")

def subir_ambiente():
    print("\nSubindo o ambiente...")
    os.system("docker-compose up --build")

def derrubar_conteiners():
    print("\nDerrubando os contêineres...")
    os.system("docker-compose down")

def limpar_ambiente():
    print("\nLimpando o ambiente...")
    os.system("docker compose down --rmi all --volumes --remove-orphans")

def verificar_container(nome_container):
    resultado = subprocess.run(
        ["docker", "ps"], capture_output=True, text=True
    )
    return nome_container in resultado.stdout

def testar_ping():
    print("\nExecutando teste de Ping...")
    if verificar_container("roteador"):
        os.system("cd roteador/test && python teste_ping.py")
    else:
        print("ERRO: Os containers não estão em execução. Execute 'Subir o ambiente' primeiro.")

def testar_rotas():
    print("\nExecutando teste de Rotas...")
    if verificar_container("roteador"):
        os.system("cd roteador/test && python teste_rotas.py")
    else:
        print("ERRO: Os containers não estão em execução. Execute 'Subir o ambiente' primeiro.")

def testar_vias():
    print("\nExecutando teste de Vias...")
    if verificar_container("roteador"):
        os.system("cd roteador/test && python teste_vias.py")
    else:
        print("ERRO: Os containers não estão em execução. Execute 'Subir o ambiente' primeiro.")

def testar_ping_host():
    print("\nExecutando teste de Ping entre Hosts...")
    if verificar_container("host"):
        os.system("cd host/script_teste && python teste_ping.py")
    else:
        print("ERRO: Os containers não estão em execução. Execute 'Subir o ambiente' primeiro.")

def testar_limiares():
    print("\nExecutando teste de Limiares...")
    if verificar_container("roteador"):
        os.system("cd roteador/test && python limiares.py")
    else:
        print("ERRO: Os containers não estão em execução. Execute 'Subir o ambiente' primeiro.")

def menu():
    while True:
        try:
            print("\nEscolha a ação que deseja executar:")
            print("1 - Gerar o arquivo docker-compose.yml")
            print("2 - Subir o ambiente")
            print("3 - Derrubar os contêineres")
            print("4 - Limpar o ambiente")
            print("5 - Testar Ping")
            print("6 - Testar Rotas")
            print("7 - Testar Vias")
            print("8 - Testar Ping entre Hosts")
            print("9 - Testar Limiares")
            print("0 - Sair")

            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                gerar_compose()
            elif escolha == "2":
                subir_ambiente()
            elif escolha == "3":
                derrubar_conteiners()
            elif escolha == "4":
                limpar_ambiente()
            elif escolha == "5":
                testar_ping()
            elif escolha == "6":
                testar_rotas()
            elif escolha == "7":
                testar_vias()
            elif escolha == "8":
                testar_ping_host()
            elif escolha == "9":
                testar_limiares()
            elif escolha == "0":
                derrubar_conteiners()
                print("Saindo do programa...")
                break
            else:
                print("\nOpção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nOperação interrompida pelo usuário. Retornando ao menu principal...")

if __name__ == "__main__":
    menu()
