#!/bin/bash
#
### BEGIN INIT INFO
# Provides:          Lades
# Required-Start:    
# Required-Stop:     
# Should-Start:      
# Should-Stop:       
# Default-Start:     
# Default-Stop:      
# Short-Description: Sincroniza regras do yara no Cuckoo sandobox
# Description:       Sincroniza regras disponibilizadas pela comunidade
#		     no yara do Cuckoo Sandbox local
### END INIT INFO
#

#set -e
#set -u

#Cria o diretorio quando nao existir

GITYARA="gitYaraCommunity"
BASEDIR=/opt/$GITYARA

if [ ! -d $BASEDIR ]; then
	echo "Diretorio nao encontrado. Criando diretorio..."
	mkdir $BASEDIR -m 775

	#clona o repositório remoto
	echo "Clonando repositorio remoto"
	git clone https://github.com/citizenlab/malware-signatures.git $BASEDIR
fi

#Diretorio padrao do git
cd $BASEDIR

#Atualiza com o repositorio remoto
git pull

#realiza a copia das assinaturas da comunidade para o Cuckoo local
cp -rf /opt/gitYaraCommunity/yara-rules/malware-families /opt/cuckoo/cuckoo/data/yara/

echo "include \"/opt/cuckoo_saltar/data/yara/binaries/shellcodes.yar\"" > /opt/cuckoo_saltar/data/yara/index_binaries.yar
echo "include \"/opt/cuckoo_saltar/data/yara/binaries/embedded.yar\"" >> /opt/cuckoo_saltar/data/yara/index_binaries.yar
echo "include \"/opt/cuckoo_saltar/data/yara/binaries/vmdetect.yar\"" >> /opt/cuckoo_saltar/data/yara/index_binaries.yar
echo "include \"/opt/cuckoo_saltar/data/yara/malware-families/\"" >> /opt/cuckoo_saltar/data/yara/index_binaries.yar




