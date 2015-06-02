#!/usr/bin/python2
#-*- coding: utf-8 -*-

import json
import operator
import sys
import os
CHARS = ['/', ':','-', '!', '_', '(', ')', '[', ']', '{', '}']
BASE_PATH = ''


def update_pcap_name(json_file, folder_task):


	try:
		open(folder_task+'/dump.pcap',r)
		try:
			f = open(json_file, 'r')
			content = json.load(f)
		except:
			return

		print 'Renaming PCAP file for task '+folder_task	
		os.rename(folder_task+'/dump.pcap', folder_task+'/'+content['target']['file']['name']+'.pcap')
	except:
		print 'file not exists'

if __name__ == "__main__":

    path = sys.argv[1]
    
    if os.path.isfile(path):
    	print 'diretorio errado'
    else:

        files = [ path + '/' + f for f in os.listdir(path)  if os.path.isfile(os.path.join(path,f+'/reports/report.json')) ]
        for f in files:
            update_pcap_name(f+'/reports/report.json', f) 

