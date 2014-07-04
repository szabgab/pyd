from __future__ import print_function, division
import urllib2, feedparser

#import pkg_resources

rss_feed = 'https://pypi.python.org/pypi?%3Aaction=rss'
def run():
	url = urllib2.urlopen(rss_feed)
	rss = url.read()
	#print(rss);
	feed = feedparser.parse( rss )
	print(feed)
	
	# fetch the rss feed
	# list the most recent package names and version numbers
	# fetch the json file of each package
	# http://pypi.python.org/pypi/<package_name>/json
    # http://pypi.python.org/pypi/<package_name>/<version>/json
	# download each package
	# unzip them


#    check_dist('pydigger')
#    print(hi())

#def hi():
#    return "Hi from PyDigger"
#
#def check_dist(dist_name):
#    try:
#        bm = pkg_resources.get_distribution(dist_name)
#    except pkg_resources.DistributionNotFound:
#        print("Distribution '{}' not found".format(dist_name))
#        return
#
#    print(bm.requires())
#    print(bm.version)

