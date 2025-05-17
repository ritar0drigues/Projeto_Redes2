import subprocess
import re 
class Manipulacao:
    
    @staticmethod
    def roteadores_encontrados():
        comando = "docker ps --filter name=roteador --format '{{.Names}}'"
        result = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
        roteadores = [r.strip("'") for r in result.stdout.split('\n') if r]
        return roteadores

    # destino_ip = Manipulacao.extrair_subnet_roteador_ip(destino)
    # prox_salto_ip = Manipulacao.extrair_ip_roteadores_ip(prox_salto)
    
    @staticmethod
    def extrair_numero_roteador(roteador_name):
        return f"172.21.{int(roteador_name.split('roteador')[-1]) - 1}"
    
    @staticmethod
    def extrair_numero_roteador_ip(ip_roteador):
        ip_ini = ip_roteador.split('.')[:-1]
        
        return '.'.join(ip_ini) 
    
    @staticmethod
    def extrair_subnet_roteador_ip(ip_roteador):
        return f"{Manipulacao.extrair_numero_roteador_ip(ip_roteador)}.0/24"
    
    @staticmethod
    def extrair_ip_roteadores_ip(ip_roteador):
        return f"{Manipulacao.extrair_numero_roteador_ip(ip_roteador)}.2"
    
    @staticmethod
    def extrair_subnet_roteador(roteador_name):
        return f"{Manipulacao.extrair_numero_roteador(roteador_name)}.0/24"
    
    @staticmethod
    def extrair_ip_roteadores(roteador_name):
        return f"{Manipulacao.extrair_numero_roteador(roteador_name)}.2"
    
    @staticmethod
    def extrair_ip_gateway(roteador_name):
        return f"{Manipulacao.extrair_numero_roteador(roteador_name)}.1"
    
    @staticmethod
    def extrair_linhas(resultado):
        linhas = resultado.split('\n')
        return linhas
    
    @staticmethod
    def traduzir_caminho(roteador, caminho, qtd_roteadores=0):
        hops = Manipulacao.extrair_linhas(caminho)
        traducao = []
        traducao.append(roteador)           
        for hop in hops[1:]:
            if 'roteador' in hop:
                nome_roteador = hop.split()[1].split('.')[0]
                traducao.append(nome_roteador)
            elif hop and '(' in hop and ')' in hop:
                try:
                    n1, n2 = hop.split('(')[1].split(')')[0].split('.')[2:]
                    numero_roteador = 0
                    if n2 == '4':
                        numero_roteador = int(n1) + 2
                        if numero_roteador > qtd_roteadores:
                            numero_roteador = numero_roteador % qtd_roteadores
                    elif n2 == '3':
                        numero_roteador = int(n1)
                        if numero_roteador > qtd_roteadores:
                            numero_roteador = numero_roteador % qtd_roteadores
                    else:
                        numero_roteador = int(n1) + 1
                    traducao.append(f'roteador{numero_roteador}')
                except (ValueError, IndexError):
                    # Handle unexpected hop format gracefully
                    continue
        
        return ' -> '.join(traducao)
    
if __name__ == "__main__":
    # Teste da classe Manipulacao
    ip = '172.21.1.2'
    
    print(Manipulacao.extrair_numero_roteador_ip(ip))
    print(Manipulacao.extrair_subnet_roteador_ip(ip))
    print(Manipulacao.extrair_ip_roteadores_ip(ip))