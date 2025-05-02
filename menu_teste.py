import os

def menu():
    while True:
        try:
            print("\nEscolha a ação que deseja executar:")
            print("1 - Gerar o arquivo docker-compose.yml (gerar_compose)")
            print("2 - Subir o ambiente (all)")
            print("3 - Derrubar os contêineres (down)")
            print("4 - Limpar o ambiente (clean)")
            print("5 - Testar Ping (teste_ping)")
            print("6 - Testar Rotas (teste_rotas)")
            print("7 - Testar Vias (teste_vias)")
            print("8 - Testar Ping entre Hosts (teste_ping_host)")
            print("9 - Sair")
            
            escolha = input("Digite o número da opção desejada: ")
            
            if escolha == "1":
                print("\nGerando o arquivo docker-compose.yml...")
                os.system("make gerar_compose")
            elif escolha == "2":
                print("\nSubindo o ambiente...")
                os.system("make all")
            elif escolha == "3":
                print("\nDerrubando os contêineres...")
                os.system("make down")
            elif escolha == "4":
                print("\nLimpando o ambiente...")
                os.system("make clean")
            elif escolha == "5":
                print("\nExecutando teste de Ping...")
                os.system("make teste_ping")
            elif escolha == "6":
                print("\nExecutando teste de Rotas...")
                os.system("make teste_rotas")
            elif escolha == "7":
                print("\nExecutando teste de Vias...")
                os.system("make teste_vias")
            elif escolha == "8":
                print("\nExecutando teste de Ping entre Hosts...")
                os.system("make teste_ping_host")
            elif escolha == "9":
                print("\nSaindo...")
                break
            else:
                print("\nOpção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nOperação interrompida pelo usuário. Retornando ao menu principal...")

if __name__ == "__main__":
    menu()