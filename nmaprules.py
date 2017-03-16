#!/usr/bin/python

class Classifier:
    pass

rules = []
def rule(fn):
    rules.append(fn)
    return fn

def classifier(name):
    def classifier_as(fn):
        def fnRule(rec):
            if fn(rec):
                rec[4].append(name)
        rule(fnRule)
        return fn
    return classifier_as

@rule
def initialize(rec):
    rec.append([])

@classifier('dns')
def isDns(rec):
    return rec[2] == "domain" or rec[1].startswith('53/')

@classifier('ike')
def isIke(rec):
    return rec[1].startswith('500/')

@classifier('ntp')
def isNtp(rec):
    return rec[1].startswith('123/') or rec[2] == 'ntp'

@classifier('smtp')
def isSmtp(rec):
    return rec[1].startswith('25/') or 'smtp' in rec[2]

@classifier('snmp')
def isSnmp(rec):
    return rec[1].startswith('161/udp') or rec[2] == 'snmp'

@classifier('ssh')
def isSsh(rec):
    return rec[1] == '22/tcp' or rec[2] == 'ssh'

@classifier('ssl')
def isSsl(rec):
    return 'ssl' in rec[2]

@classifier('telnet')
def isTelnet(rec):
    return rec[1] == '23/tcp'

@classifier('http')
def isHttp(rec):
    return 'http' in rec[2] and not isSsl(rec)

@classifier('https')
def isHttps(rec):
    return 'http' in rec[2] and isSsl(rec)

@classifier('sip')
def isSip(rec):
    return 'sip' in rec[2]

@rule
def wrappedRule(rec):
    if rec[2] == 'tcpwrapped':
        rec[4] = ['nc']

@rule
def elseRule(rec):
    if len(rec[4])==0:
        rec[4] = ['unknown']

def classify(data):
    for rec in data:
        for rule in rules:
            rule(rec)

