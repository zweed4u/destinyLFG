import requests
import BeautifulSoup
url='http://www.destinylfg.com/php/search.php?console=XB360&activity=%25&textSearch=&mic=false&lfg_type=%25&light=%25'

resp=requests.get(url)
soup=BeautifulSoup.BeautifulSoup(resp.content)

print '####################################################################'
	
listing=soup.findAll('div', {'class':'guardian-listing clearfix'})
for info in listing: 
	print '\n'
	#print info.contents[0].findAll('div',{'class':'guardian-info'})[0]
	gt=info.contents[0].findAll('div',{'class':'guardian-info'})[0].findAll("kbd")[0].text
	subclass=info.contents[0].findAll('div',{'class':'guardian-info'})[0].findAll('span',{'class':'class'})[0].text
	level= info.contents[0].findAll('div',{'class':'guardian-info'})[0].findAll('span',{'class':'level'})[0].text	
	light=info.contents[0].findAll('div',{'class':'guardian-info'})[0].findAll('span',{'class':'light'})[0].text
	activity = info.contents[1].findAll('span')[0].text
	description = info.contents[1].findAll('p',{'class':'p-comment small'})[0].text
	lang = info.contents[2].findAll('span',{'class':'guardian-language'})[0].text
	timestamp = info.contents[2].findAll('span',{'class':'time-stamp'})[0].text
	print gt,' :: ',subclass,' :: ',level,' (',light,')'
	print activity
	print '>',description
	print lang,' :: ',timestamp
	print '\n'
	print '####################################################################'	
print '\n'
