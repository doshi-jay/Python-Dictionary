import urllib2
from bs4 import BeautifulSoup
import requests

x = 0
_file = open("gre_words.txt","r")
_file3 = open("done_words.txt",'r+')
_file2 = open("gre_meanings.html","a")
temp = _file.readlines()
done = _file3.readlines()
print done
try:
	temp.remove('\n')
except ValueError, v:
	x = 1 

word_number =  len(done) + 1	

_file2.write('<span style="font-family:Cambria;font-size:15">')	
for val in temp:
	if val in done:
		x = 2
	else:	
		val = str(val.replace('\n',''))
		url = 'http://www.merriam-webster.com/dictionary/' + str(val)  	
		response = requests.get(url)
		html = response.content
		soup = BeautifulSoup(html,'lxml')
		raw_records = soup.find_all('ol',class_='definition-list')
		_file2.write("<hr><h2><u>" + str(word_number) + " : " +  val + "</u></h2></hr><br>")
		for r in raw_records:
			# t = r.get_text().encode('utf-8')
			t = r.encode('utf-8')
			t.replace('&nbsp;','')
			_file2.write('<p >' + str(t) + '</p>')
			_file2.write('<br/>')
		
		_file2.write('<br/>')
		_file2.write('<br/>')
		_file3.write(val + "\n")
		word_number = word_number + 1


_file2.write('</span>')
	