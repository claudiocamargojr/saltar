#!/usr/bin/python2
#-*- coding: utf-8 -*-

import json
import operator
import sys
from name_generator import Guesser
import os
CHARS = ['/', ':','-', '!', '_']

def parse(json_file):
	g = Guesser()
	f = open(json_file, 'r')
	s = json.load(f)


	tags = {}
	total = 0
	fname = json_file[:-5]


	out = {}
	noPathFileName = os.path.basename(json_file)
	out['filename'] = noPathFileName[:-4]
	out['analysis'] = s

	for key in s:
		value = s[key].lower()
		tmp = value
		
		for char in CHARS:
			tmp = tmp.replace(char, '.')

		words = tmp.split('.')


		for word in words:
			total += 1
			if word in tags:
				tags[word] += 1
			else:
				tags[word] = 1


	
	sorted_tags = [ (x[0], float(x[1]) / total) for x in (sorted(tags.items(), key=operator.itemgetter(1)))]
	
	out['tags'] = [x[0] for x in sorted_tags[-5:] ]
	out['tags_weight'] = [x[1] for x in sorted_tags[-5:] ]
	#Adding the ml classification
	out['ml_classification'] = g.guess_everything(s)


	print (json.dumps(out, indent=2))



if __name__ == "__main__":

	path = sys.argv[1]

	if os.path.isfile(path):
		parse(path)
	else:
		files = [ path + '/' + f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
		for f in files:
			parse(f)

		
