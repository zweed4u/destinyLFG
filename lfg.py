import mechanize
import urllib
import cookielib
import BeautifulSoup
import html2text
import re
import sys





print ""
print 'Activity? (atheon h, templar h, conflux h, oracles h, gorgon h, crota n, ir yut n, crota h, 32poe, 34,poe, 35poe, nf) '
activity = raw_input('')

print ""
				
if activity == "atheon h":
	act = 'Vault+of+Glass+-+Hard+(Atheon)'
elif activity == "templar h":
	act = 'Vault+of+Glass+-+Hard+(Templar)'
elif activity == "conflux h":
	act = 'Vault+of+Glass+-+Hard+(Conflux)'
elif activity == "oracles h":
	act = 'Vault+of+Glass+-+Hard+(Oracles)'
elif activity == "gorgon h":
	act = 'Vault+of+Glass+-+Hard+(Gorgon%27s+Labyrinth)'
elif activity == "crota n":
	act = 'Crota%27s+End+-+Normal+(Crota)'
elif activity == "ir yut n":
	act = 'Crota%27s+End+-+Normal+(Deathsingers)'
elif activity == "crota h":
	act = 'Crota%27s+End+-+Hard+(Crota)'
elif activity == "32poe":
	act = 'Prison+of+Elders+-+Lvl+32'
elif activity == "34poe":
	act = 'Prison+of+Elders+-+Lvl+34'
elif activity == "35poe":
	act = 'Prison+of+Elders+-+Lvl+35'
elif activity == "nf":
	act = 'Weekly+Nightfall+Strike'
else:
	print "Rerun and enter one of the above"

i=0
url=""

# Browser
br = mechanize.Browser()



# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)



# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)



# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Chrome')]




try:

	#act = 'Social' #TEST~~~~~~~~~~~~
	url = "http://www.destinylfg.com/php/search.php?console=Xbox+360&activity="+str(act)+"&textSearch=&mic=false&lfg_type=%25"
	
	br.open(str(url))
	# Inspect name of the form
	# Select the second (index one) form - the first form is a search query box


	#br.select_form(nr=0)
		    
	#scrape page for anything in span tag
	htmltext = br.open(str(url)).read()

	regex='<kbd>(.+?)</kbd>'
	pattern = re.compile(regex)
	gamertag = re.findall(pattern,htmltext)

	regex2='<span class="level">(.+?)</span>'
	pattern2 = re.compile(regex2)
	level = re.findall(pattern2,htmltext)

	regex3='<span class="class">(.+?)</span>'
	pattern3 = re.compile(regex3)
	char = re.findall(pattern3,htmltext)

	regex4='<p class="p-comment small">(.+?)</p>'
	pattern4 = re.compile(regex4)
	description = re.findall(pattern4,htmltext)
	

	amount = len(gamertag)
	
	regex5='<strong><span>(.+?)</span></strong>'
	pattern5 = re.compile(regex5)
	title = re.findall(pattern5,htmltext)
	

	regex6='<span class="time-stamp">(.+?)</span>'
	pattern6 = re.compile(regex6)
	timestamp = re.findall(pattern6,htmltext)
	
	
	
	class color:
		PURPLE = '\033[95m'
		CYAN = '\033[96m'
		DARKCYAN = '\033[36m'
		BLUE = '\033[94m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
		END = '\033[0m'

	#print url

	print color.UNDERLINE + color.BOLD + title[0] + color.END
	'''print amount
	print str(gamertag)
	print i'''
	while i < amount:
		print "GT: "+str(gamertag[i])+"\nClass: "+str(char[i])+"\nLevel: "+str(level[i])+"\nDescription: "+str(description[i])+"\nTimestamp: "+str(timestamp[i])+"\n\n"
		i+=1
		

except:
	print str(gamertag)
	print str(description)
	print "~~~EXCEPTION~~~\n"
	#if raised outputs product id and page url w/ redirection (if any)
	print "No users are running    -> " + str(activity) +" <-    - "+ str(br.geturl())+"\n"
	#os.system("pause")



