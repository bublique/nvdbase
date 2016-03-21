#!/usr/bin/python3
import xml.etree.ElementTree as ET
import sys
import re
from xml.dom import minidom


if __name__ == '__main__':
	xmldoc=minidom.parse (sys.argv[1])
	cvsslist = xmldoc.getELementsByTagName('cvss:base_metrics')
	print (cvslist)
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
