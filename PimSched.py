#!/usr/bin/env python2
#PimSched is an application that schedules vocabulary/facts according to the Pimsleur approach(google that), using the unofficial Google TTS "API" for synthesizing the vocabulary
#Version 0.4

#(current version) complete rewrite: Elon Bing, June 2015
#(initial release) author: Elon Bing(rayman), May 2012
#Bugfix: Elon Bing(rayman), Dec 2012 (added "not indeling.has_key(cursor)" to line 87)

import re

try: #If argparse is installed on this machine (Python>=2.7), use that library
	import argparse
except ImportError: #If not, use the included library
	from included_libraries import argparse


from PimSched_libraries.libpimsched import Lesson, IdiomTuple

parser = argparse.ArgumentParser(description='PimSched is an application that schedules vocabulary/facts according to the Pimsleur approach(google that), using the unofficial Google TTS "API" for synthesizing the vocabulary', version='0.4')
parser.add_argument('language1', help='The ISO-abbreviation(English=en, German=de, etc) for the language of the words before the \'=\' sign')
parser.add_argument('language2', help='The ISO-abbreviation(English=en, German=de, etc) for the language of the words before the \'=\' sign')
parser.add_argument('wordlist',help='A file containing vocabulary and translations seperated by \'=\'.')
parser.add_argument('-o','--outputpath',required=False, type=str, help='Path for the output .mp3 file. Default=./result.mp3', default='./result.mp3')

args=parser.parse_args()
woordjesfile=open(args.wordlist)
woordjeslines=woordjesfile.readlines()
woordjesfile.close()

outputpath=args.outputpath
languages = [args.language1, args.language2]

idioms=[]
for line in woordjeslines:
    if not '=' in line:
        continue
    
    idioms.append((IdiomTuple(languages[0], line.split('=')[0]), IdiomTuple(languages[1], line.split('=')[1])))

l = Lesson()
for idiompair in idioms:
    l.add(idiompair)

l.exportaudio(outputpath)
