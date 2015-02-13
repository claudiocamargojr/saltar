
__author__ = 'SALTAR'
__version__ = '1.0'

import dpkt
import socket
import pygeoip
import optparse 

geoInfo=pygeoip.GeoIP('/home/claudio/Documents/GeoLiteCity.dat')

def detalhaInfoIP(ip):
    try:
        rec=geoInfo.region_by_name(ip)
        cidade=rec['cidade']
        pais=rec['pais']
        if cidade !='':
            geoLocalizacao=cidade + ', ' + pais
        else:
            geoLocalizacao=pais
        return geoLocalizacao
    except Exception as e:
        print ('Nao registrado')

def exibirPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth=dpkt.ethernet.Ethernet(buf)
            ip=eth.data
            origem=socket.inet_ntoa(ip.src)
            destino=socket.inet_ntoa(ip.dest)
            print ("Origem: " + origem + " ---> Destino: " + destino)
            print ("Origem: " + detalhaInfoIP(origem) + " ---> Destino: " + detalhaInfoIP(destino))
        except:
            pass

def main():
    parser=optparse.OptionParser('usage%prog -p <arquivo pcap>')
    parser.add_option('-p', dest='arquivoPcap', type='string', help='Especifique o arquivo de formato pcap')
    (options, args)=parser.parse.args()
    if options.arquivoPcap==None:
        print (parser.usage)
        exit (0)
    arquivoPcap=options.arquivoPcap
    f=open(arquivoPcap)
    pcap=dpkt.pcap.Reader(f)
    exibirPcap(pcap)
    
    
if __name__=="__main__":
    main()
