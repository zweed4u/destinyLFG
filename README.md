# destinyLFG  
<p align="center">
  <img src="https://raw.githubusercontent.com/zweed4u/destinyLFG/master/lfgcombanner.jpg" alt="Find a Fireteam!"/>
</p>
Overview:  
Recently, I have become very fond of Bungie's new game "Destiny". However, for those of us that don't use our gaming systems to socialize and have a lacking friend's list on PSN/XBL, it's somewhat of a pain to coordinate and get more people to join your 'fireteam' for mandatory multiplayer parts. Luckily, there is a website that allows users to post for groups. This is a scraper for a 'looking for group' site. At the moment it only supports a limited amount of popular activities, but in the future I plan to expand support and allow for all actvities.


Technical:  
This python script is a scraper that makes use of a backend php link that queries for posts on the lfg's server. This requires mechanize and beautifulsoup as well as some other basic libraries. (see imports in top of file)


Issues:  
Updating support for all consoles presented a problem in that parsing a large group of listings caused the scrape to trip up and cause the description to match with the proper listing. Near updates will be focused on proper exception handling and attempts to resolve this. As it is now, I display all entries in an array after the pretty print in an exception to cover all bases.  

##Taken King 2.0 release!
With the celebration of year 2, many things have been added and/or modified. This has also subsequently rendered some of the functionality temporarily broken. Fixes will be on the way.  



Contact me with any questions: [@ZWeed4U](http://www.twitter.com/zweed4u)
