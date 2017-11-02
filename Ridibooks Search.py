# -*- coding:utf-8 -*-

from HTMLParser import HTMLParser

import urllib
import json
import unicodedata
import BeautifulSoup as bs

def getPrettyString (string):
	resultString = string
	
	resultString = resultString.replace ('<strong class="title_point">', ' ')
	resultString = resultString.replace ('</strong>', ' ')
	resultString = resultString.replace('\n', '')
	resultString = resultString.strip()
	
	return resultString

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

q = u'{query}'
q2 = unicodedata.normalize('NFC', q)
q3 = urllib.quote(q2.encode('utf-8'))

unparsed = urllib.urlopen(u'https://ridibooks.com/search/?q={0}'.format(q3)).read()
soup = bs.BeautifulSoup(unparsed.encode('utf-8', 'ignore'))

resultList = soup.findAll("span", "title_text")
resultCount = len (resultList)


print "<items>"

if resultCount > 0:
	for i in range (0, resultCount):
		element = resultList[i]
		elementCount = len (element)
		resultTitle = ""
		resultTag = ""
		for j in range (0, elementCount):
			resultTitle += (str(element.contents[j]))
		
		resultTitle = getPrettyString(resultTitle)
		resultTag = '<item uid="%s" arg="%s"><title>%s</title><subtitle>상세 페이지는 아직 못가요 미안..</subtitle><icon>icon.png</icon></item>' % (q, q, resultTitle)
		print resultTag
else:
	print '<item uid="noitem" arg="noitem"><title>검색 결과가 없습니다</title><subtitle>미안해요..</subtitle><icon>icon.png</icon></item>' % (q, q, resultTitle)

print "</items>"