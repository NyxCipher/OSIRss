import feedparser

class WhizRssAggregator():
	feedurl = ""

	# Credits:
	#
	# Tutorial Source: https://medium.com/@DigitallyMani/how-to-build-a-rss-parser-in-python-2879135dc2d6
	# Tutorial Author: Mani Gopalakrishnan
	#

	def __init__(self, paramrssurl):
		print(paramrssurl)
		self.feedurl = paramrssurl

	def parse(self):
		thefeed = feedparser.parse(self.feedurl)

		print("Getting Feed Data")
		print(thefeed.feed.get("title", ""))
		print(thefeed.feed.get("link", ""))
		print(thefeed.feed.get("description", ""))
		print(thefeed.feed.get("published", ""))
		#print(thefeed.feed.get("published_parsed", thefeed.feed.published_parsed))

		for thefeedentry in thefeed.entries:
			print("__________")
			print(thefeedentry.get("guid", ""))
			print(thefeedentry.get("title", ""))
			print(thefeedentry.get("link", ""))
			print(thefeedentry.get("description", ""))
			print("__________")

			#for thefeednamespace in thefeed.namespaces:
			#	if (thefeednamespace == "media"):
			#		print("Media")
			#		allmediacontent = thefeedentry.get("media_content", "")
			#		for themediacontent in allmediacontent:
			#			print(themediacontent["url"])
			#			print(themediacontent["height"])
			#			print(themediacontent["width"])