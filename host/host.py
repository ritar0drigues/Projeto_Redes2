import time
import socket
import subprocess
import os

meu_nome = socket.gethostname()
meu_ip = socket.gethostbyname(meu_nome)

if __name__ == "__main__":
    print(f"[{meu_nome}] Iniciado com IP {meu_ip}.")
    roteador_conectado = os.environ["ROTEADOR_CONECTADO"]
    

    subprocess.run("ip route del default", check=True, shell=True)
    

    subprocess.run(f"ip route add default via {roteador_conectado} dev eth0", check=True, shell=True)
        
    print(f"Rota default configurada via {roteador_conectado}")
    
    while True:
        time.sleep(1)