
set -e


if [ -z "$ROTEADOR_CONECTADO" ]; then
  echo "A variável ROTEADOR_VIZINHO não está definida!"
  exit 1
fi


ip route del default

ip route add default via "$ROTEADOR_CONECTADO" dev eth0

ip route show

exec sleep infinity