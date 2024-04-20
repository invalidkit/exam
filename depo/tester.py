from parser import HtmlParser
import re

nbuparser = HtmlParser('https://bank.gov.ua/')
nbuparser.NbuParse('div', 'index-page')
print(nbuparser.Result)

tempparser1 = HtmlParser('https://sinoptik.ua')
tempparser1.TempParse('td', 'p1')
tempparser2 = HtmlParser('https://sinoptik.ua')
tempparser2.TempParse('td', 'p2')
tempparser3 = HtmlParser('https://sinoptik.ua')
tempparser3.TempParse('td', 'p3')
tempparser4 = HtmlParser('https://sinoptik.ua')
tempparser4.TempParse('td', 'p4')
tempparser5 = HtmlParser('https://sinoptik.ua')
tempparser5.TempParse('td', 'p5')
tempparser6 = HtmlParser('https://sinoptik.ua')
tempparser6.TempParse('td', 'p6')
tempparser7 = HtmlParser('https://sinoptik.ua')
tempparser7.TempParse('td', 'p7')
tempparser8 = HtmlParser('https://sinoptik.ua')
tempparser8.TempParse('td', 'p8')

ls = [tempparser1.Result[2], tempparser2.Result[2], tempparser3.Result[2], tempparser4.Result[2], tempparser5.Result[2], tempparser6.Result[2], tempparser7.Result[2], tempparser8.Result[2]]

print(ls)
