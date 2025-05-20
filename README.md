# Projeto de Simulação de Rede de Computadores

Este projeto implementa uma simulação de rede usando Python e Docker, com foco em roteamento e comunicação entre hosts.

## Como Executar o Projeto

### Pré-requisitos
- Docker instalado
- Python 3.8
- pip (gerenciador de pacotes Python)
- Bibliotecas Python adicionais: matplotlib, networkx, seaborn

### Passos para Execução

1. Clone o repositório
2. Execute o menu de controle:
```bash
python menu_teste.py
```

O menu oferece as seguintes opções:
1. Gerar arquivo docker-compose.yml
2. Subir o ambiente
3. Derrubar os contêineres
4. Limpar o ambiente
5. Testar Ping
6. Testar Rotas
7. Testar Vias
8. Testar Ping entre Hosts
9. Testar Limiares
0. Sair

### Fluxo de Execução Recomendado
1. Primeiro, gere o compose (opção 1)
2. Suba o ambiente (opção 2)
3. Execute os testes desejados (opções 5-9)
4. Ao finalizar, use a opção 0 para sair e limpar o ambiente

## Protocolo Utilizado

O projeto utiliza o protocolo UDP (User Datagram Protocol) para comunicação entre hosts e roteadores.

### Justificativa do Protocolo

O UDP foi escolhido pelos seguintes motivos:
- Baixa latência na comunicação entre hosts
- Simplicidade na implementação do roteamento
- Menor overhead de processamento
- Adequado para simulações de rede em tempo real
- Eficiente para testes de conectividade e roteamento

## Como a Topologia é Construída

### Estrutura Base
- Hosts: Pontos finais da rede
- Roteadores: Responsáveis pelo encaminhamento de pacotes
- Docker Networks: Simulam as conexões físicas

### Tipos de Topologias Suportadas
- Estrela
- Anel
- Totalmente conectada
- Árvore
- Linha

### Processo de Construção
1. O arquivo gerar_yaml.py define a estrutura da rede
2. docker_compose_create.py gera o arquivo de configuração do Docker
3. Os containers são criados representando hosts e roteadores
4. As redes Docker são estabelecidas conforme a topologia escolhida

### Gerenciamento
- Cada host possui um IP único na rede
- Os roteadores implementam o algoritmo de estado de enlace
- A comunicação é testada através de pings e verificação de rotas

## Funcionamento da Rede

### Comunicação Entre Hosts
- Hosts podem se comunicar apenas através dos roteadores
- Cada host está conectado a um roteador específico
- A comunicação entre hosts em diferentes redes passa pelo algoritmo de roteamento
- O caminho entre hosts é determinado pelos roteadores intermediários

### Algoritmo de Roteamento
- Implementação do protocolo Link State (Estado de Enlace)
- Propagação automática de informações de roteamento (LSA)
- Atualização dinâmica das tabelas de roteamento
- Detecção de falhas e recálculo de rotas

## Testes e Monitoramento

### Ping Entre Hosts
- Verifica conectividade básica entre hosts
- Mostra tempos de resposta e falhas
- Indica problemas de roteamento

### Teste de Rotas
- Verifica tabelas de roteamento
- Mostra caminhos disponíveis
- Identifica gargalos na rede

### Teste de Vias
- Análise de caminhos alternativos
- Verificação de redundância
- Teste de failover

### Teste de Limiares
- Gera matriz de tempos de resposta
- Cria mapa de calor da rede
- Visualiza estado das conexões
- Identifica pontos de falha

### Arquivos de Diagnóstico
- matriz_ping.png: Visualização dos tempos de resposta
- grafico_rede.png: Estado atual da topologia
- Logs de teste no terminal

### Arquivos Gerados
Os testes geram dois arquivos de visualização:
- matriz_ping.png: Mapa de calor usando escala de azuis para tempos de resposta, marcando falhas em vermelho com texto "FALHA"
- grafico_rede.png: Grafo da rede com nós em azul claro, conexões bem-sucedidas em verde e falhas em vermelho

