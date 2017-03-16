#!/usr/bin/python


from nmaptools import NmapResults
from sys import argv
from json import dumps

results = NmapResults()
results.open(argv[1:])
print dumps(results.data)
