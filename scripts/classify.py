#!/usr/bin/python2
#-*- coding: utf-8 -*-

import json
import operator
import sys
import os
CHARS = ['/', ':','-', '!', '_', '(', ')', '[', ']', '{', '}']
BASE_PATH = ''
ALIASES={'w32':'win32', 'trj':'trojan','troj':'trojan','trojan2':'trojan','troj2':'trojan', 'gen':'generic', 'androidos':'android','w64':'win64'}

def parse(json_file, base_dir):
    s = None
    try:
        f = open(json_file, 'r')
        s = json.load(f)
    except:
        return

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
        tmp = value.replace(' ', '')
        
        for char in CHARS:
            tmp = tmp.replace(char, '.')

        words = tmp.split('.')


        for word in words:
            if not word:
                continue
            if ALIASES.has_key(word):
            	word=ALIASES[word]    
            total += 1
            if tags.has_key(word):
                tags[word] += 1
            else:
                tags[word] = 1

    sorted_tags = [ (x[0], float(x[1]) / total) for x in (sorted(tags.items(), key=operator.itemgetter(1)))]
    
#    for tag in sorted_tags:
#        print tag
    out['tags'] = [x[0] for x in sorted_tags[-5:] ]
    out['tags_weight'] = [x[1] for x in sorted_tags[-5:] ]
    content= json.dumps(out, indent=2)
    
    target = open(base_dir + '/' + fname + '.json', 'w')
    target.write(content)
    target.close()


if __name__ == "__main__":

    path = sys.argv[1]
    target_path = sys.argv[2]

    if os.path.isfile(path):
        parse(path, target_path)
    else:

        files = [ path + '/' + f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
        for f in files:
            parse(f, target_path)

