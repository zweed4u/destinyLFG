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
	con = 'Xbox+360'
elif console == "4":
	con = 'Xbox+One'
else:
	print "Rerun and enter one of the listed numbers above..."
	sys.exit()


print color.UNDERLINE+color.BOLD+'Activity?'+color.END+'\n1.) Atheon (HARD)\n2.) Templar (HARD)\n3.) Defend the Confluxes (HARD)\n4.) Oracles (HARD)\n5.) Gorgon Maze (HARD)\n6.) Crota Boss (NORM)\n7.) Ir Yut, the Deathsinger (NORM)\n8.) Crota Boss (HARD)\n9.) Lvl 32 Prison of Elders\n10.) Lvl 34 Prison of Elders\n11.) Lvl 35 Prison of Elders\n12.) Weekly Nightfall Stike\n13.) Trials of Osiris \n\nPlease enter a number: '




activity = raw_input('')
print ""

				
if activity == "1":
	act = 'Vault+of+Glass+-+Hard+(Atheon)'
	activity = "Atheon (HARD)"
elif activity == "2":
	act = 'Vault+of+Glass+-+Hard+(Templar)'
	activity = "Templar (HARD)"
elif activity == "3":
	act = 'Vault+of+Glass+-+Hard+(Conflux)'
	activity = "Defend the Confluxes (HARD)"
elif activity == "4":
	act = 'Vault+of+Glass+-+Hard+(Oracles)'
	activity = "Oracles (HARD)"
elif activity == "5":
	act = 'Vault+of+Glass+-+Hard+(Gorgon%27s+Labyrinth)'
	activity = "Gorgon Maze (HARD)"
elif activity == "6":
	act = 'Crota%27s+End+-+Normal+(Crota)'
	activity = "Crota Boss (NORM)"
elif activity == "7":
	act = 'Crota%27s+End+-+Normal+(Deathsingers)'
	activity = "Ir Yut, the Deathsinger (NORM)"
elif activity == "8":
	act = 'Crota%27s+End+-+Hard+(Crota)'
	activity = "Crota Boss (HARD)"
elif activity == "9":
	act = 'Prison+of+Elders+-+Lvl+32'
	activity = "Lvl 32 Prison of Elders"
elif activity == "10":
	act = 'Prison+of+Elders+-+Lvl+34'
	activity = "Lvl 34 Prison of Elders"
elif activity == "11":
	act = 'Prison+of+Elders+-+Lvl+35'
	activity = "Lvl 35 Prison of Elders"
elif activity == "12":
	act = 'Weekly+Nightfall+Strike'
	activity = "Weekly Nightfall Stike"
elif activity == "13":
	act= 'Trials+of+Osiris+-+Competitive'
	activity = "Trials of Osiris"
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
br.addheaders = [('User-agent', 'Chrome')]




try:
	#Setting act variable for testing purposes...
	#act = 'Social' 
	url = "http://www.destinylfg.com/php/search.php?console="+str(con)+"&activity="+str(act)+"&textSearch=&mic=false&lfg_type=%25"
	
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



