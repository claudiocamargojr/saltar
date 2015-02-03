__author__ = 'Claudio'


import zipfile
import optparse
from threading import Thread

def extrairArquivo(arquivoZip, senha):
    try:
        arquivoZip.extractall(pwd=senha)
        print ("A senha foi descoberta: " + senha)
    except Exception as e:
        print (e)


def main():
    parser=optparse.OptionParser("usage%prog " + \
        "-f <arquivoZip> -d <dicionario>")
    parser.add_option('-f', dest='nomeArquivoZip', type='string', help='especifique o arquivo compactado')
    parser.add_option('-d', dest='arquivoDicionario', type='string', help='especifique o arquivo de dicionario')

    (options, args)=parser.parse_args()

    if (options.nomeArquivoZip==None) | (options.arquivoDicionario==None):
            print (parser.usage)
            exit(0)
    else:
        nomeArquivoZip=options.nomeArquivoZip
        arquivoDicionario=options.arquivoDicionario

        arquivoZip=zipfile.ZipFile(nomeArquivoZip)
        dicionario=open(arquivoDicionario)

        for line in dicionario.readlines():
            senha=line.strip('\n')
            print ('senha usada: ' + senha)
            t=Thread(target=extrairArquivo, args=(arquivoZip,senha))
            t.start()


if __name__=="__main__":
    main()
