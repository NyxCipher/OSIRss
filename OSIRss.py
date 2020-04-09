"""
__author__ = "it0bsession"
__copyright__ = "Copyright 2020, OpenSource InfoSecRss [OSIRSS]"
__credits__ = ["Luis Borralho(InfoSec Resource List: Hackin9 Magazine)", "Mani Gopalakrishnan(WizRssAggregator)", "it0bsession(Dev)"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "it0bsession"
__status__ = "Beta"
"""

from WhizRssAggregator import WhizRssAggregator
import webbrowser

URL = ""
title = ""
website = ""

def printTitle():
	print(title)

def rssObject():
	rssobject=WhizRssAggregator(URL).parse()

menu = {}
menu ['1'] = "OpenStack"
menu ['2'] = "OSVDB"
menu ['3'] = "Pentester.es"
menu ['4'] = "SecList"
menu ['5'] = "Pentest Geek"
menu ['6'] = "Zend Framework Security"
menu ['7'] = "Lamians"
menu ['8'] = "Tactical Web Application Security"
menu ['9'] = "PacketStorm"
menu ['10'] = "SANS Internet Storm Center"
menu ['11'] = "CXSecurity Exploits"
menu ['12'] = "CXSecurity Vulnerabilities"
menu ['13'] = "CXSecurity CVEProducts"
menu ['14'] = "National Vulnerability Databas"
menu ['15'] = "Errata Security"
menu ['16'] = "Fortinet Blog"
menu ['17'] = "Security Intelligence"
menu ['18'] = "Vulners"
menu ['19'] = "Securelist"
menu ['20'] = "Naked Security"
menu ['21'] = "Android Central"
menu ['22'] = "Schneier on Security"
menu ['23'] = "Threatpost"
menu ['24'] = "Security Advisories"
menu ['25'] = "Packet Storm"
menu ['26'] = "Toolswatch"
menu ['27'] = "Citrix"
menu ['28'] = "Vulnerability Lab Rss"
menu ['29'] = "Vulnerability Lab News"
menu ['30'] = "Vulnerability Lab Bounty"
menu ['31'] = "Vulnerability Lab db"
menu ['0'] = "Exit"
menu ['00'] = "Browser"
while True:
	options = menu.keys()
	sorted(options)
	for entry in options:
			print (entry, menu[entry])

	selection = input("Please Select: ")
	if selection == '1':
		print ("OpenStack")
		URL = "https://www.openstack.org/blog/?feed=rss2"
		rssObject()
	elif selection == '2':
		print ("OSVDB")
		URL = "https://blog.osvdb.org/feed/"
		rssObject()
	elif selection == '3':
		print ("Pentester.es")
		URL = "https://www.pentester.es/feed"
		rssObject()
	elif selection == '4':
		menu2 = {}
		menu2 ['1'] = "Nmap Development"
		menu2 ['2'] = "Nmap Announce"
		menu2 ['3'] = "Full Disclosure"
		menu2 ['4'] = "BugTraq"
		menu2 ['5'] = "Security Basics"
		menu2 ['6'] = "Penetration Testing"
		menu2 ['7'] = "Info Security News"
		menu2 ['8'] = "Firewall Wizards"
		menu2 ['9'] = "IDS Focus"
		menu2 ['10'] = "Web App Security"
		menu2 ['11'] = "Daily Dave"
		menu2 ['12'] = "PaulDotCom"
		menu2 ['13'] = "Honeypots"
		menu2 ['14'] = "Microsoft See Notification"
		menu2 ['15'] = "Funsee"
		menu2 ['16'] = "CERT Advisiors"
		menu2 ['17'] = "Open Source Security"
		menu2 ['18'] = "Secure Coding"
		menu2 ['19'] = "Educause Security Discussion"
		menu2 ['20'] = "NANOG"
		menu2 ['21'] = "Intersting People"
		menu2 ['22'] = "The RISKS Forum"
		menu2 ['23'] = "BreachExchange"
		menu2 ['24'] = "Metasploit"
		menu2 ['25'] = "Wireshark"
		menu2 ['26'] = "Snort"
		menu2 ['0' ] = "Return"
		while True:
			options2 = menu2.keys()
			sorted(options2)
			for entry in options2:
				print (entry, menu2[entry])

			selection2 = input("Please Select: ")
			if selection2 == '1':
				title = "Nmap Development"
				URL = "https://seclists.org/rss/nmap-dev.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '2':
				title = "Nmap Announce"
				URL = "https://seclists.org/rss/nmap-announce.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '3':
				title = "Full Disclosure"
				URL = "https://seclists.org/rss/fulldisclosure.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '4':
				title = "BugTraq"
				URL = "https://seclists.org/rss/bugtraq.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '5':
				title = "Security Basics"
				URL = "https://seclists.org/rss/basics.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '6':
				title = "Penetration Testing"
				URL = "https://seclists.org/rss/pen-test.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '7':
				title = "Info Security News"
				URL = "https://seclists.org/rss/isn.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '8':
				title = "Firewall Wizards"
				URL = "https://seclists.org/rss/firewall-wizards.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '9':
				title = "IDS Focus"
				URL = "https://seclists.org/rss/focus-ids.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")
				
			elif selection2 == '10':
				title = "Web App Security"
				URL = "https://seclists.org/rss/webappsec.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '11':
				title = "Daily Dave"
				URL = "https://seclists.org/rss/dailydave.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '12':
				title = "PaulDotCom"
				URL = "https://seclists.org/rss/pauldotcom.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '13':
				title = "Honeypots"
				URL = "https://seclists.org/rss/honeypots.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")
				
			elif selection2 == '14':
				title = "Microsoft See Notification"
				URL = "https://seclists.org/rss/microsoft.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '15':
				title = "Funsee"
				URL = "https://seclists.org/rss/funsec.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '16':
				title = "CERT Advisiors"
				URL = "https://seclists.org/rss/cert.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '17':
				title = "Open Source Security"
				URL = "https://seclists.org/rss/oss-sec.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")
				
			elif selection2 == '18':
				title = "Secure Coding"
				URL = "https://seclists.org/rss/securecoding.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")
			elif selection2 == '19':
				title = "Educause Security Discussion"
				URL = "https://seclists.org/rss/educause.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '20':
				title = "NANOG"
				URL = "https://seclists.org/rss/nanog.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '21':
				title = "Intersting People"
				URL = "https://seclists.org/rss/interesting-people.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")
				
			elif selection2 == '22':
				title = "The RISKS Forum"
				URL = "https://seclists.org/rss/risks.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '23':
				title = "BreachExchange"
				URL = "https://seclists.org/rss/dataloss.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '24':
				title = "Metasploit"
				URL = "https://seclists.org/rss/metasploit.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '25':
				title = "Wireshark"
				URL = "https://seclists.org/rss/wireshark.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")
				
			elif selection2 == '26':
				title = "Snort"
				URL = "https://seclists.org/rss/snort.rss"
				printTitle()
				rssObject()
				input("Press Enter to continue...")

			elif selection2 == '0':
				break

			else:
				print ("Unknown Selection")

	elif selection == '5':
		print ("Pentest Geek")
		URL = "https://www.pentestgeek.com/blog/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '6':
		print ("Zend Framework Security")
		URL = "https://framework.zend.com/security/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '7':
		print ("Lamians")
		URL = "https://getlaminas.org/blog/rss.xml"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '8':
		print ("Tactical Web Application Security")
		URL = "http://tacticalwebappsec.blogspot.com/feeds/posts/default"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '9':
		print ("PacketStorm")
		URL = "http://rss.packetstormsecurity.com"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '10':
		print ("SANS Internet Storm Center")
		URL = "https://isc.sans.edu/xml.html"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '11':
		print ("CXSecurity Exploits")
		URL = "https://cxsecurity.com/wlb/rss/exploit/"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '12':
		print ("CXSecurity Vulnerabilities")
		URL = "https://cxsecurity.com/wlb/rss/vulnerabilities/"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '13':
		print ("CXSecurity CVEProducts")
		URL = "https://cxsecurity.com/cveproducts/"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '14':
		print ("National Vulnerability Database")
		URL = "https://www.nist.gov/news-events/nist-rss-feeds"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '15':
		print ("Errata Security")
		URL = "https://blog.erratasec.com/feeds/posts/default"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '16':
		print ("Fortinet Blog")
		URL = "https://www.fortinet.com/rss-feeds.html"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '17':
		print ("Security Intelligence")
		URL = "https://securityintelligence.com/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '18':
		print ("Vulners")
		URL = "https://vulners.blog/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '19':
		print ("Securelist")
		URL = "https://securelist.com/feed/"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '20':
		print ("Naked Security")
		URL = "https://nakedsecurity.sophos.com/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '21':
		print ("Android Central")
		URL = "https://www.androidcentral.com/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '22':
		print ("Schneier on Security")
		URL = "https://www.schneier.com/blog/atom.xml"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '23':
		print ("Threatpost")
		URL = "https://threatpost.com/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '24':
		print ("Security Advisories")
		URL = "https://www.tenable.com/blog/feed"
		rssObject()
		input("Press Enter to continue...")


	elif selection == '25':
		print ("Packet Storm")
		URL = "https://packetstormsecurity.com/feeds"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '26':
		print ("Toolswatch")
		URL = "http://www.toolswatch.org/feed"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '27':
		print ("Citrix")
		URL = "http://www.citrix.com/events.rss"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '28':
		print ("Vulnerability Lab Rss")
		URL = "https://www.vulnerability-lab.com/rss/rss.php"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '29':
		print ("Vulnerability Lab News")
		URL = "https://www.vulnerability-lab.com/rss/rss_news.php"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '30':
		print ("Vulnerability Lab Bounty")
		URL = "https://www.vulnerability-lab.com/rss/rss_bounty.php"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '31':
		print ("Vulnerability Lab db")
		URL = "https://www.vulnerability-db.com/?q=rss.xml"
		rssObject()
		input("Press Enter to continue...")

	elif selection == '0':
		break
	elif selection == '00': 
		website = input("Enter a URL: ")
		webbrowser.open_new(website)
		
	else:
			print ("Unknown Selection")

