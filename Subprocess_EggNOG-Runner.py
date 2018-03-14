import os
import subprocess
import sys

if len(sys.argv)<2:
    print "USAGE: python directory and output file. "
    sys.exit()

directory = sys.argv[1]


for files in os.listdir(directory):
    outfile= files[:-3] + 'out'
    if files.endswith('.faa'):
        print files
        cmd = ['python',  'emapper.py', '-i', files, '--output', outfile,'-m', 'diamond', '--cpu','10' ]
        print cmd
        subprocess.call(cmd)
print 'Done'
