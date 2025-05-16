all:
	@docker-compose up --build
	
gerar_compose:
	@cd gera_yml && pip install --quiet -r requirements.txt
	@cd gera_yml && python gerar_yaml.py
	@cd gera_yml && python docker_compose_create.py

down:
	@docker-compose down 
	
clean:
	docker compose down --rmi all --volumes --remove-orphans

teste_ping:
	@if docker ps | grep -q "roteador"; then \
		cd docker/roteador/test && python teste_ping.py; \
	else \
		echo "ERRO: Os containers não estão em execução. Execute 'make all' primeiro."; \
		exit 1; \
	fi

teste_rotas:
	@if docker ps | grep -q "roteador"; then \
		cd docker/roteador/test && python teste_rotas.py; \
	else \
		echo "ERRO: Os containers não estão em execução. Execute 'make all' primeiro."; \
		exit 1; \
	fi

teste_vias:
	@if docker ps | grep -q "roteador"; then \
		cd docker/roteador/test && python teste_vias.py; \
	else \
		echo "ERRO: Os containers não estão em execução. Execute 'make all' primeiro."; \
		exit 1; \
	fi

teste_ping_host:
	@if docker ps | grep -q "host"; then \
		cd docker/host/script_teste && python teste_ping.py; \
	else \
		echo "ERRO: Os containers não estão em execução. Execute 'make all' primeiro."; \
		exit 1; \
	fi