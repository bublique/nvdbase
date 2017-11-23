#!/usr/bin/python3

import xml.etree.ElementTree as ET
import sys
import re
from xml.dom import minidom
import xlsxwriter

def newfunc:
    pass

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
    fileV = open('vendors.txt', 'r')
    #fileS = open('Expenses01.xlsx', 'rw')
    colnames = [
        'id',
        'publisheddate',
        'score',
        'access-vector',
        'access-complexity',
        'authentication',
        'confidentiality-impact',
        'integrity-impact',
        'availability-impact',
        'source',
        'generated-on-datetime',
        #'product',  Расскомеентить если будут продукты
        'summary',
        'vendor']

    col = 0
    row = 0
    for n in colnames:
        worksheet.write(row, col, n)
        col = col+1
    row = 1

    vendors = {}
    for v in map(str.rstrip, fileV.readlines()):
        vendors[v] = 0

    for entry in iterate_children(xmldoc.firstChild):
        summary = entry.getElementsByTagNameNS(vuln, 'summary')[0].firstChild.data
        for v in vendors.keys():
            if v in summary:
                vendors[v] += 1

                col = 0
                worksheet.write(row, col, entry.getElementsByTagNameNS(vuln, 'cve-id')[0].firstChild.data)
                col=col+1
                worksheet.write(row, col, entry.getElementsByTagNameNS(vuln, 'published-datetime')[0].firstChild.data)
                #col=col+1
                _b = entry.getElementsByTagNameNS(cvss, 'base_metrics')
                if _b == None:
                    continue
                if len(_b) == 0:
                    continue
                base_metrics = _b[0]
                for metric in iterate_children(base_metrics):
                    col = col+1
                    worksheet.write(row, col, metric.firstChild.data)
                col=col+1
                worksheet.write(row, col, entry.getElementsByTagNameNS(vuln, 'summary')[0].firstChild.data)
                col=col+1
                worksheet.write(row,col,v)
                #col=col+1    
                #worksheet.write(row, col, entry.getElementsByTagNameNS(vuln, 'product')[0].firstChild.data)    берет просто первый продукт из списка. не нужное.  
                row = row+1

    print(vendors)
    workbook.close()
