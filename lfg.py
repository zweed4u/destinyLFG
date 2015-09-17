import mechanize
import urllib
import cookielib
import BeautifulSoup
import html2text
import re
import sys

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
print "\n"
print "  ____            _   _             _     _____ ____	"
print " |  _ \  ___  ___| |_(_)_ __  _   _| |   |  ___/ ___|	"
print " | | | |/ _ \/ __| __| | '_ \| | | | |   | |_ | |  _ 	"
print " | |_| |  __/\__ \ |_| | | | | |_| | |___|  _|| |_| |	"
print " |____/ \___||___/\__|_|_| |_|\__, |_____|_|   \____|	"
print "                              |___/                  	"
print "                                            		"         
print "           ````                   `````     		"         
print "        .sdNMMNds:`           `-+hNMMMmy:   		"     
print "       :NMMMMMMMMMN` `+yhho-  dMMMMMMMMMMo  		"     
print "       yMMMMMMMMMMM. dMMMMMN. NMMMMMMMMMMN`  		"     
print "       +NMMMMMMMMMM. MMMMMMM/ NMMMMMMMMMMh   		"     
print "        :hNMMMMMMMM.`MMMMMMM/ NMMMMMMMNd+`   	 	"     
print "          .+dMMMMMM- MMMMMMM/ NMMMMMms-`    		"     
print "            `:hMMMM+ hMMMMMm..MMMMm+`       		"     
print "               /mMMN+.+yyyo-:dMMMs`         		"     
print "                .mMMMmyooosdNMMN/           		"     
print "                 -NMMMMMMMMMMMM+            		"     
print "                  sMMMMMMMMMMMm             		"     
print "                  .MMMMMMMMMMMo             		"     
print "                   mMMMMMMMMMM-             		"     
print "                   oMMMMMMMMMh              		"     
print "                    +mMMMMMNs`              		"     
print "                      .:::-`                		"     
print ""
print ""

print color.UNDERLINE+color.BOLD+'Console?'+color.END+'\n1.) PS3\n2.) PS4\n3.) xBox 360\n4.) xBox One\n\nPlease enter a number: '

console = raw_input('')
print ""

if console == "1":
	con = 'PS3'
elif console == "2":
	con = 'PS4'
elif console == "3":
	con = 'XB360'
elif console == "4":
	con = 'XB1'
else:
	print "Rerun and enter one of the listed numbers above..."
	sys.exit()

#need to update
print color.UNDERLINE+color.BOLD+'Activity?'+color.END+'\n1.) Atheon (HARD)\n2.) Crota Boss (NORM)\n3.) Crota Boss (HARD)\n4.)Prison of Elders\5.) Weekly Nightfall Stike\n\nPlease enter a number: '


activity = raw_input('')
print ""

#need to update/add php links - 2.0			
if activity == "1":
	act = 'Vault+of+Glass+-+Hard+(Atheon)'
	activity = "Atheon (HARD)"
elif activity == "2":
	act = 'Crota%27s+End+-+Normal+(Crota)'
	activity = "Crota Boss (NORM)"
elif activity == "3":
	act = 'Crota%27s+End+-+Hard+(Crota)'
	activity = "Crota Boss (HARD)"
elif activity == "4":
	act = 'Prison+of+Elders'
	activity = "Prison of Elders"
elif activity == "5":
	act = 'Nightfall'
	activity = "Weekly Nightfall Stike"

''' INCLUDE full raids and checkpoints as well as court of oryx
elif activity == "6":
	act = 'Daily+-+Heroic+Story'
	activity = "Daily Heroic"
elif activity == "7":
	act = 'King%27s+Fall+-+Normal+(Full+Raid)'
	activity = "King's Fall Full Raid (NORM)"
elif activity == "8":
	act = 'King%27s+Fall+-+Normal+(Oryx)'
	activity = "King's Fall Oryx (NORM)"
elif activity == "9":
	act = 'King%27s+Fall+-+Hard+(Full+Raid)'
	activity = "King's Fall Full Raid (HARD)"
elif activity == "10":
	act = 'King%27s+Fall+-+Hard+(Oryx)'
	activity = "King's Fall Oryx (HARD)"
elif activity == "11":
	act = 'Court+of+Oryx+T1'
	activity = "Court of Oryx Tier 1"
elif activity == "12":
	act = 'Court+of+Oryx+T2'
	activity = "Court of Oryx Tier 2"
elif activity == "13":
	act = 'Court+of+Oryx+T3'
	activity = "Court of Oryx Tier 3"
elif activity == "12":
	act = 'Patrol+-+Dreadnaught'
	activity = "Patrol Dreadnaught"
elif activity == "13":
	act = 'PvP+-+Trials+of+Osiris'
	activity = "Trials of Osiris"
'''

else:
	print "Rerun and enter one of the listed numbers above..."
	sys.exit()


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
br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; AskTB5.6)')]



try:
	#Setting act variable for testing purposes...
	#act = 'Social' 
	url = "http://www.destinylfg.com/php/search.php?console="+str(con)+"&activity="+str(act)+"&textSearch=&mic=false&lfg_type=%25&light=%25"
	#nice check of php link->
	#print url
	br.open(str(url))
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
	
	

	print color.UNDERLINE + color.BOLD + title[0] + color.END

	while i < amount:
		print "GT: "+str(gamertag[i])+"\nClass: "+str(char[i])+"\nLevel: "+str(level[i])+"\nDescription: "+str(description[i])+"\nTimestamp: "+str(timestamp[i])+"\n\n"
		i+=1
 		

except:
	print "Gamertags found: "+str(gamertag)
	print "Descriptions found: "+str(description)
	print "~~~EXCEPTION~~~\n"
	print "No users are running    -> " + str(activity) +" <-    - "+ str(br.geturl())+"\n"
	sys.exit()



