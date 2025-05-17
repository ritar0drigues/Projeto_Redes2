import subprocess
import sys
import os
import re
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.manipulacao import Manipulacao
from classes.mensagem import Mensagem

def executar_teste_ping():
    """
    Executa o teste de ping entre roteadores e retorna os resultados incluindo tempos de resposta
    """
    falhas = []
    sucessos = []
    tempos_ping = {}  
    
    roteadores = Manipulacao.roteadores_encontrados()
    
   
    matriz_tempos = {}
    for r_origem in roteadores:
        matriz_tempos[r_origem] = {}
        for r_destino in roteadores:
            matriz_tempos[r_origem][r_destino] = float('inf')
    
    for r_origem in roteadores:
        print(f"Testando {r_origem}...")
        for r_destino in roteadores:
            try:
                ip = Manipulacao.extrair_ip_roteadores(r_destino)
                
                comando = f"docker exec {r_origem} ping -c 3 -W 1 {ip}"
                result = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
                
                if result.returncode == 0:
                    
                    output = result.stdout
                    
                    match = re.search(r'min/avg/max\S*\s=\s\d+\.\d+/(\d+\.\d+)', output)
                    if match:
                        tempo_medio = float(match.group(1))
                    else:
                       
                        match = re.search(r'time=(\d+\.\d+)\s*ms', output)
                        tempo_medio = float(match.group(1)) if match else 0
                    
        
                    matriz_tempos[r_origem][r_destino] = tempo_medio
                    
                    print(Mensagem.formatar_sucesso(f"{r_origem} -> {r_destino}  sucesso ({tempo_medio:.2f} ms)."))
                    sucessos.append([r_origem, r_destino])
            except subprocess.CalledProcessError as e:
                print(Mensagem.formatar_erro(f"{r_origem} -> {r_destino}  falhou."))
                falhas.append([r_origem, r_destino])
               
            
        print('\n')
        
    if falhas:
        print("Roteadores com falha:")
        for roteador, destino in falhas:
            print(Mensagem.formatar_erro(f"{roteador} -> {destino}  falhou."))
        print('\n')
        
    return roteadores, sucessos, falhas, matriz_tempos

def gerar_matriz_tempos_ping(roteadores, matriz_tempos):
    """
    Gera uma matriz de calor (heatmap) mostrando os tempos de ping entre roteadores
    """
    
    roteadores_list = list(roteadores)
    n = len(roteadores_list)
    matriz_np = np.zeros((n, n))
    
  
    for i, origem in enumerate(roteadores_list):
        for j, destino in enumerate(roteadores_list):
            matriz_np[i, j] = matriz_tempos[origem][destino]
    
   
    matriz_np[matriz_np == float('inf')] = 20
    
   
    mask = matriz_np >= 20
    
   
    sns.set(style="white")
    
   
    plt.figure(figsize=(14, 12))
    
    
    ax = sns.heatmap(matriz_np, 
                     annot=True, 
                     fmt=".2f", 
                     cmap="Blues", 
                     mask=mask,
                     cbar_kws={'label': 'Tempo de Resposta (ms)'},
                     xticklabels=roteadores_list,
                     yticklabels=roteadores_list)
    
  
    for i in range(n):
        for j in range(n):
            if mask[i, j]:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='red', lw=2))
                ax.text(j + 0.5, i + 0.5, "FALHA", ha='center', va='center', color='red', fontweight='bold')
    
    plt.title('Matriz de Tempo de Ping Entre Roteadores (ms)', pad=20)
    plt.xlabel('Roteador Destino')
    plt.ylabel('Roteador Origem')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    
    plt.savefig('matriz_ping.png')
    print("Matriz de tempo de ping salva como 'matriz_ping.png'")
    
def gerar_grafico_rede(roteadores, sucessos, falhas):
    """
    Gera um gráfico de rede mostrando as conexões bem-sucedidas e com falha entre roteadores
    """
    G = nx.DiGraph()
    
    
    for roteador in roteadores:
        G.add_node(roteador)
    
    
    for origem, destino in sucessos:
        G.add_edge(origem, destino, color='green', weight=1)
    
   
    for origem, destino in falhas:
        G.add_edge(origem, destino, color='red', weight=0.5)
    
 
    edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    
   
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, seed=42)  
    

    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    
 
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=1.5, 
                          arrowsize=15, connectionstyle='arc3,rad=0.1')
    
 
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
   
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], color='green', lw=2, label='Conexão bem-sucedida'),
        Line2D([0], [0], color='red', lw=2, label='Falha de conexão')
    ]
    plt.legend(handles=legend_elements)
    
    plt.title('Mapa de Conectividade entre Roteadores')
    plt.axis('off')
    plt.tight_layout()
    
   
    plt.savefig('grafico_rede.png')
    print("Gráfico de rede salvo como 'grafico_rede.png'")

def main():
   
    print("Iniciando teste de ping entre roteadores...")
    roteadores, sucessos, falhas, matriz_tempos = executar_teste_ping()
    
   
    print("\nGerando gráficos dos resultados...")
    gerar_matriz_tempos_ping(roteadores, matriz_tempos)
    gerar_grafico_rede(roteadores, sucessos, falhas)
    
    print("\nAnálise concluída! Arquivos de gráficos gerados.")
    
if __name__ == "__main__":
    main()