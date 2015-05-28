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
# Short-Description: Sincroniza assinaturas do Cuckoo sandobox
# Description:       Sincroniza assinaturas disponibilizadas pela comunidade
#		     no Cuckoo Sandbox local
### END INIT INFO
#

#set -e
#set -u

#Cria o diretorio quando nao existir

GITCUCKOO="gitCuckooCommunity"
BASEDIR=/opt/$GITCUCKOO

if [ ! -d $BASEDIR ]; then
	echo "Diretorio nao encontrado. Criando diretorio..."
	mkdir $BASEDIR -m 775

	#clona o repositório remoto
	echo "Clonando repositorio remoto"
	git clone https://github.com/cuckoobox/community.git $BASEDIR/community
fi

#Diretorio padrao do git
cd $BASEDIR/community

#Atualiza com o repositorio remoto
git pull

#realiza a copia das assinaturas da comunidade para o Cuckoo local
cp -rf /opt/gitCuckooCommunity/community/modules/signatures/* /opt/cuckoo_saltar/modules/signatures/




