
import datetime
import uuid
import PyRSS2Gen

FEEDLOC = "/home/hkpdev008/jobstatus.rss"
DATALOC = "/home/hkpdev008/l16/jobstatus.txt"
TITLE = "Job Status"
LINK = "http://104.197.206.32/"
DESCRIPTION = "My job statuses"



# read datefile to get the latest updates
data_file = open(DATALOC)
items = []
while 1:
    line = data_file.readline()
    if not line:
       break
    desc = line
    rss_item = PyRSS2Gen.RSSItem(
        title = "Job Status",
        link = "http://104.197.206.32/",
        description = desc,
        pubDate = datetime.datetime.now(),
        guid = "http://104.197.206.32/"
        )
    items.append(rss_item)


# build the rss feed
rss_feed = PyRSS2Gen.RSS2 (
    title = TITLE,
    link = LINK,
    description = DESCRIPTION,
    lastBuildDate = datetime.datetime.utcnow(),
    items = items
    )

print rss_feed.to_xml()
