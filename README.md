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

## Testes Disponíveis
- Ping entre hosts
- Verificação de rotas
- Teste de vias de comunicação
- Conectividade entre hosts e roteadores
- Análise de limiares da rede

### Teste de Limiares
O teste de limiares realiza medições de conectividade e gera duas visualizações:
- Um mapa de calor (heatmap) mostrando os tempos de resposta de ping entre todos os roteadores, com indicações de falhas
- Um grafo direcionado mostrando a topologia da rede e o estado de todas as conexões

### Arquivos Gerados
Os testes geram dois arquivos de visualização:
- matriz_ping.png: Mapa de calor usando escala de azuis para tempos de resposta, marcando falhas em vermelho com texto "FALHA"
- grafico_rede.png: Grafo da rede com nós em azul claro, conexões bem-sucedidas em verde e falhas em vermelho

