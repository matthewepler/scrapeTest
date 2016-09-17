#scraper using Python 3 (ideally, or 2.7 optionally),

#Pycurl or the python requests library, and BeautifulSoup (bs4) to be used to collect all posts from all the pages of this thread in this forum:

#http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591

#Required fields are: post id, name, date of the post (in text form or as is) and post body.

#Output the results to a spreadsheet file named forum.csv

#An example of a single post in that file should look like the following:

#87120;&quot;Rick&quot;;&quot;Mon Sep 24, 2012 4:53 pm&quot;;&quot;Tonight, 8pm, might be worth a look...?\n\nRJ&quot;


##
##

# Finding posts
# - - - - - - - - - -
# DOM Node structure of post - pertinent details only
#<tr>
#	<td...><span class="name"><a name={"#####"}></a><b>{"nameString"}</b></span>...</td> 
#	<td...>
#		<table...>
#			<tr>
#				<td...><a href="viewtopic.php?p={#####}#{#####}">...<span class="postdetails">"Posted: {DateString}"<span...></span></span></td>
#				<td...><a href="posting.php?{mode=quote}&p={#####}">...</td>
#			</tr>
#			<tr>
#				<td...>
#			</tr>
#			<tr>
#				<td...><span class="postbody">{textString}...</span><span class="gensmall"></span></td>
#			</tr>
#		</table>
#	</td>
#</tr>


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import csv

def writeToCSV(posts):
	with open('posts.csv', 'w') as csvfile:
		fieldnames = ['id', 'name', 'date', 'body']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()
		for p in posts:
			writer.writerow(p)

		print('file write complete')


def getPostData(node, idNode):
		idTag = node.find(lambda tag: tag.has_attr('name'))
		if idTag != None:				
			postId = idTag['name']
		else:
			postId = "notFound"	

		# alt method, get id from 'viewtopic...' URL
		#idStrings = re.compile('p=\d{5}').findall(idNode['href'])
		#if ( len(idStrings) > 0 ):
		#	postId = idStrings[0].split('=')[1]

		name = idTag.find_next_sibling().get_text()

		dateString = idNode.find_next_sibling().get_text().split('\xa0')[0]
		date = dateString.replace('Posted: ', '')

		body = parseBody(node.find('span', class_='postbody'))

		postData = {
			'id'  : postId,
			'name': name,
			'date': date,
			'body': body
		}

		return postData


def parseBody(node):
	bodyText = node.get_text().strip()

	if len(bodyText) < 1:
			return parseBody( node.find_next('span', class_='postbody') )

	if ('_________________' in bodyText):
		body = bodyText.split('_________________')[0].strip()
	else:
		body = bodyText
	
	return body.replace('\n', '').replace('\r', '')


def getPosts(url, params):
	global allPosts

	paramString = '?'
	for p in params:
		paramString += p + '=' + params[p] + '&'

	paramString = paramString[:-1]
	requestUrl = url + paramString

	pagePosts = []

	try:
		# breaking params does not break request
		html = urlopen(requestUrl)
		bs = BeautifulSoup(html, 'lxml')

		try:
			postGroup = bs.find('table', class_='forumline')
		except:
			print('<table class="forumline"> not found')

			print(requestUrl)
			return False;

		for node in postGroup:
			if (node.name != None):
				# id also appears in a tags with 'name' attribute, but I think the php link is a stronger search criteria. True?
				idNode = node.find('a', href=re.compile(r'(viewtopic\.php\?p=)\d{5}'))
				if (idNode != None):
					post = getPostData(node, idNode)
					pagePosts.append(post)

	except:
		print('Request Error: ' + requestUrl)	
		return False

	if len(pagePosts) > 0:
		allPosts.extend(pagePosts)
		print( len(pagePosts), 'posts collected')
		return True
	else:
		return False


# --------------------------------
#       		MAIN
# --------------------------------
topicId = 12591
startIndex = 0 
indexPagination = 15
baseUrl = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php' 
params = {
	't' : str(topicId),
	'postdays' : '0',
	'postorder' : 'asc',
	'start' : str(startIndex)
}

allPosts = []

print('requesting posts', startIndex, 'to', startIndex + indexPagination)

while getPosts(baseUrl, params): 
	startIndex += indexPagination
	params['start'] = str(startIndex)
	print('requesting posts', startIndex, 'to', startIndex + indexPagination)

print('** DONE **')
print( len(allPosts), 'posts collected TOTAL' )

if (len(allPosts) > 0):
	writeToCSV(allPosts)	
else:
	print('No posts found.')

















