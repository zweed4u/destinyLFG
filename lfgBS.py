import sys, requests, BeautifulSoup


print '1. Xbox360'
print '2. XboxOne'
print '3. PS4'
print '4. PS3'
print '5. All'
console=raw_input('Which console? (enter number) ')
if console =='1':
	print 'Xbox360'
	con='XB360'
elif console =='2':
	print 'XboxOne'
	con='XB1'
elif console =='3':
	print 'PS4'
	con='PS4'
elif console =='4':
	print 'PS3'
	con='PS3'
elif console =='5':
	print 'Searching through all...'
	con='%25'
else:
	print 'Please rerun and choose appropriate number.'
	sys.exit()
url='http://www.destinylfg.com/php/search.php?console='+con+'&activity=%25&textSearch=&mic=false&lfg_type=%25&light=%25'
print url
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
	if con=='%25':
		con='All'
	print con,' :: ',lang,' :: ',timestamp
	print '\n'
	print '####################################################################'	
print '\n'
