#!/usr/bin/python3
import xml.etree.ElementTree as ET
import sys
import re
from xml.dom import minidom
import xlsxwriter

def namespaceResolve(xmldoc, nspace):
    nvd = xmldoc.getElementsByTagName('nvd')[0]
    return nvd.getAttribute('xmlns:' + nspace)

def iterate_children(parent):
    child = parent.firstChild
    while child != None:
        if (isinstance(child, minidom.Element)):
                yield child
        child = child.nextSibling

if __name__ == '__main__':
    xmldoc=minidom.parse (sys.argv[1])
    vuln = namespaceResolve(xmldoc, 'vuln')
    cvss = namespaceResolve(xmldoc, 'cvss')

    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet()

    colnames = [
        'id',
        'score',
        'access-vector',
        'access-complexity',
        'authentication',
        'confidentiality-impact',
        'integrity-impact',
        'availability-impact',
        'source',
        'generated-on-datetime']

    col = 0
    row = 0
    for n in colnames:
        worksheet.write(row, col, n)
        col = col+1

    row = 1
    for entry in iterate_children(xmldoc.firstChild):
        col = 0
        worksheet.write(row, col, entry.getElementsByTagNameNS(vuln, 'cve-id')[0].firstChild.data)
        _b = entry.getElementsByTagNameNS(cvss, 'base_metrics')
        if _b == None:
            continue
        if len(_b) == 0:
            continue
        base_metrics = _b[0]
#       col = 0
#       if row == 0:
#           for metric in iterate_children(base_metrics):
#               col = col+1
#           #    worksheet.write(row, col, metric.tagName)
#           row = row+1
        for metric in iterate_children(base_metrics):
            col = col+1
            worksheet.write(row, col, metric.firstChild.data)
        row = row+1
    workbook.close()

    
    #cvsslist = xmldoc.getELementsByTagName('cvss:base_metrics')
    #year_re = re.compile('^CVE-2015')
    #tree = ET.parse(sys.argv[1])
    #root = tree.getroot()
    #outfile=open('viborka.txt', 'w')
    #for cvss in root:
        #bm=cvss.get('base_metrics')
        #name = cvss.get('id')
        #cvss_num = cvss.get('score')
        #for cvss2 in child:
        #cvss_num = child.get('cvss:score')
        #cvss_score = cvss.get ('score')
        #print(bm)
    #root = fromstring ('nvdcve-2.0-2015.xml')


















        #desc = child.find('summary').text'''
        #prnt(name,cvss, cvss_score)
