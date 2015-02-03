__author__ = 'Claudio'

import optparse
from socket import *
from threading import Thread

'Método que conecta a um host em uma determinada porta'
def connScan(host, porta):
    try:
        connSocket=socket(AF_INET, SOCK_STREAM)
        print ("Socket criado")
        destino=(str(host), int(porta))
        connSocket.connect(destino)
        connSocket.close()
    except Exception as e:
        print ("TCP fechado. Porta: " + porta)
        print (e)

'Método que conecta a um dispositivo por n portas diferentes, procurando uma porta que permita conexão'
def portScan(host, portas):
    for porta in portas:
        print ("Escaneando porta " + porta)
        connScan(host,porta)

setdefaulttimeout(2)


def main():
    parser=optparse.OptionParser("usage%prog " + \
        "--host <host> -p <porta alvo>")
    parser.add_option('--host', dest='hostAlvo', type='string', help='especifique o hostname ou IP alvo')
    parser.add_option('-p', dest='portaAlvo', type='string', help='especifique as portas alvo separado por vírgula (,)')

    (options, args)=parser.parse_args()


    if (options.hostAlvo==None) | (options.portaAlvo==None):
            print (parser.usage)
            exit(0)
    else:
        host=options.hostAlvo
        portaA=options.portaAlvo

        t=Thread(target=connScan, args=(host,portaA))
        t.start()


if __name__=="__main__":
    main()



