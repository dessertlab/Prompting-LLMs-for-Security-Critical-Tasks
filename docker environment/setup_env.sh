#!/bin/bash

#Fa sì che lo script fallisca appena qualcosa non va, per evitare comportamenti imprevisti
set -euo pipefail

# == Versioni testate ==
REQ_PYTHON="3.10.12"
REQ_PIP="22.0.2"
REQ_DOCKER="23.0.1"
REQ_COMPOSE="1.29.2"

# Funzione per confrontare le diverse versioni
compare_ver () {
  [ "$(printf '%s\n' "$2" "$1" | sort -V | head -n1)" = "$2" ]
}

echo "[+] Verifica prerequisiti..."

# Python
PY_VER=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
echo " - Python: $PY_VER (testato con $REQ_PYTHON)"
ver_ge "$PY_VER" "$REQ_PYTHON" || { echo "[-] Python troppo vecchio"; exit 1; }

# Pip
PIP_VER=$(pip --version | awk '{print $2}')
echo " - pip: $PIP_VER (testato con $REQ_PIP)"
ver_ge "$PIP_VER" "$REQ_PIP" || { echo "[-] pip troppo vecchio"; exit 1; }

# Docker
if ! command -v docker >/dev/null; then
  echo "[-] Docker non installato"; exit 1
fi
DK_VER=$(docker --version | awk '{print $3}' | tr -d ',')
echo " - Docker: $DK_VER (testato con $REQ_DOCKER)"
ver_ge "$DK_VER" "$REQ_DOCKER" || { echo "[-] Docker troppo vecchio"; exit 1; }

# Docker Compose
if ! docker compose version >/dev/null 2>&1 && ! docker-compose version >/dev/null 2>&1; then
  echo "[-] Docker Compose non trovato"; exit 1
fi
if command -v docker-compose >/dev/null; then
  DC_VER=$(docker-compose version --short)
else
  DC_VER=$(docker compose version --short)
fi
echo " - Docker Compose: $DC_VER (testato con $REQ_COMPOSE)"
ver_ge "$DC_VER" "$REQ_COMPOSE" || { echo "[-] Compose troppo vecchio"; exit 1; }

docker info >/dev/null 2>&1 || { echo "[-] Docker non è in esecuzione"; exit 1; }

echo "[✓] Prerequisiti verificati."



echo "[+] Installazione librerie necessarie nell’ambiente host..."

pip install --quiet \
  evaluate==0.4.5 \
  pylcs==0.1.1 \
  rouge==1.0.1 \
  nltk==3.9.1 \
  pandas==2.3.1 \
  openpyxl==3.1.5
  
echo "[✓] Librerie installate."



echo "[+] Creazione reti Docker..."

networks=(
  bot_net
  flask_net
  ftp_net
  webserver_net
  mail_net
  twitter_net
  smb_net
  proxy_net
  tcp_net
  udp_net
  ssh_net
)

for net in "${networks[@]}"; do
	if ! docker network ls --format '{{.Name}}' | grep -wq "$net"; then
		if [ "$net" == "udp_net" ]; then
			echo "  ↪ Creazione rete $net con subnet 192.168.99.0/24"
			docker network create --driver bridge --subnet 192.168.99.0/24 "$net"
		elif [ "$net" == "webserver_net" ]; then
			echo "  ↪ Creazione rete $net con subnet 172.32.0.0/24"
			docker network create --driver bridge --subnet 172.32.0.0/24 "$net"
		elif [ "$net" == "smb_net" ]; then
			echo "  ↪ Creazione rete $net con subnet 172.42.0.0/28"
			docker network create --driver bridge --subnet 172.42.0.0/28 "$net"
		else
		docker network create "$net"	
	fi
		echo "  [✓] Rete creata: $net"
	else
		echo "  [-] Rete già esistente: $net"
	fi
	done

echo "[+] Costruzione delle immagini da docker-service.yml..."

docker-compose -f docker-service.yml up --no-start

echo "[✓] Ambiente pronto. Container creati ma non avviati."
