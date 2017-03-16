#!/usr/bin/python

from nmaptools import NmapResults
from sys import argv

def help():
    print banner
    print " Usage: ./nmapparse.py results.gnmap"
    print "\n Note: This script must point to a grepable output file from nmap to work properly.\n"
    exit()
if len(argv) == 0:
    help()

results = NmapResults()
results.open(argv[1:])
results.prettyPrint()
