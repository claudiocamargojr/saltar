#!/usr/bin/python2
#-*- coding: utf-8 -*-

import json
import operator
import sys
import os
CHARS = ['/', ':','-', '!', '_']

def parse(json_file):
	f = open(json_file, 'r')
	s = json.load(f)
	#jsondecoder = json.JSONDecoder()
	#jsonobject = jsondecoder.decode(s)

	tags = {}
	total = 0
	fname = s['filename']
	del s['filename']
	del s['Most Common Class']

	out = {}
	out['filename'] = fname
	out['analysis'] = s

	for key in s:
		value = s[key].lower()
		tmp = value
		
		for char in CHARS:
			tmp = tmp.replace(char, '.')

		words = tmp.split('.')


		for word in words:
			total += 1
			if tags.has_key(word):
				tags[word] += 1
			else:
				tags[word] = 1


	
	sorted_tags = [ (x[0], float(x[1]) / total) for x in (sorted(tags.items(), key=operator.itemgetter(1)))]
	
#	for tag in sorted_tags:
#		print tag
	out['tags'] = [x[0] for x in sorted_tags[-5:] ]
	out['tags_weight'] = [x[1] for x in sorted_tags[-5:] ]
	print json.dumps(out, indent=2)


if __name__ == "__main__":

	path = sys.argv[1]

	if os.path.isfile(path):
		parse(path)
	else:
		files = [ path + '/' + f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
		for f in files:
			parse(f)

		
