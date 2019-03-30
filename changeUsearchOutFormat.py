import sys
import os

file = sys.argv[1]

open('Result/' + file + 'new','w').writelines([ line.split('\t')[0].split(' ')[0] + '\t' + line.split('\t')[1].split(' ')[0] + '\t' + '\t'.join(line.split('\t')[2:]) for line in open('Result/' + file).readlines() ])

os.remove('Result/' + file)
os.rename('Result/' + file + 'new', 'Result/' + file)