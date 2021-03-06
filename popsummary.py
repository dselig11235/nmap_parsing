#!/usr/bin/python


from nmaptools import NmapResults
from sys import argv
from json import dumps

results = NmapResults()
results.open(argv[2:])
dataStr = dumps(results.data)
funcStr = """
function addRecords(records) {
    var addButton = document.querySelector('#tabContent > form > fieldset:nth-child(8) > table:nth-child(5) > tbody:nth-child(1) > tr > td:nth-child(2) > table > tbody:nth-child(3) a');
    var rows = document.querySelectorAll('.RowdiscoveredOpenPorts');    
    var discovered = [].map.call(rows, function(r) {
        return [r.querySelector('input[name="eptOpenPortIPs"]').value, r.querySelector('input[name="eptOpenPortPorts"]').value, r.querySelector('input[name="eptOpenPortIdentifiedTypeVersions"]').value];
    });
    records.forEach(function(rec) {
        rec[1] = rec[1].toUpperCase();
        var matchPosition = discovered.findIndex(function(r) {
            return r[0] == rec[0] && r[1] == rec[1];
        });
        if(matchPosition < 0) {
            addButton.click();
            var newrows = rows[0].parentNode.children;
            var newrow = newrows[newrows.length -1 ];
            newrow.querySelector('input[name="eptOpenPortIPs"]').value = rec[0];
            newrow.querySelector('input[name="eptOpenPortPorts"]').value = rec[1];
            newrow.querySelector('input[name="eptOpenPortIdentifiedTypeVersions"]').value = rec[3];
        } else {
            rows[matchPosition].querySelector('input[name="eptOpenPortIdentifiedTypeVersions"]').value = rec[3];
        }
    });
}
"""
print '{} addRecords({})'.format(funcStr, dataStr)

funcStr = """
function addIPs(ips) {
    var t = document.querySelector('#tabContent > form > fieldset:nth-child(8) > table:nth-child(7) > tbody:nth-child(1) > tr > td:nth-child(2) > table > tbody:nth-child(2)');
    var existing = [].map.call(t.children, function(r) { 
        return r.querySelector('input[name="eptOSAssetIPs"]').value
    });
    ips.forEach(function(ip) {
        if(existing.indexOf(ip) < 0) {
            document.querySelector('#tabContent > form > fieldset:nth-child(8) > table:nth-child(7) > tbody:nth-child(1) > tr > td:nth-child(2) > table > tbody:nth-child(3) > tr > td > a').click();
            t.children[t.children.length - 1].querySelector('input[name="eptOSAssetIPs"]').value=ip;
        }
    });
}
"""

with open(argv[1]) as f:
    ips = [line.strip() for line in f.readlines()]
print '{} addIPs({})'.format(funcStr, dumps(ips));
