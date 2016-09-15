#scraper using Python 3 (ideally, or 2.7 optionally),

#Pycurl or the python requests library, and BeautifulSoup (bs4) to be used to collect all posts from all the pages of this thread in this forum:

#http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591

#Required fields are: post id, name, date of the post (in text form or as is) and post body.

#Output the results to a spreadsheet file named forum.csv

#An example of a single post in that file should look like the following:

#87120;&quot;Rick&quot;;&quot;Mon Sep 24, 2012 4:53 pm&quot;;&quot;Tonight, 8pm, might be worth a look...?\n\nRJ&quot;


##
##

# Extent, navigation
# - - - - - - - - - -
# structure of internal page link URL:
# "...viewtopic.php?" + param list
# t=[1259] -> topic number
# postdays=[0] -> default 0 for every link. change this and it breaks
# postorder=[asc] -> ascending/descending (dsc)
# start=[0] -> post number
	# a number greater than existing posts does not return error

# method 1 = find nav, find <a> with 'Next'
# method 2 = count # of posts, and use URL' start' param
	# if return does not equal increment amount(15), we're done
	# go one more and check for "No posts exist for this topic" text. if yes, great. if not, exit with error


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

# validate if true for one page

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def getPostData(node, idNode):
		print(node.name)
		#postId= idNode
		#name = node.find(lambda tag: tag.has_attr('name'))
		#date = node.find('span', class_='postdetails')
		#body = node.find('span', class_='postbody')
		#if (name != None and date != None and body != None):
		#	print(name.next_element.get_text())
		#	print(date.get_text())
		#	print('- - - ')
	# contains a.has_attr('name'), span.class="postdetails", span.class="postbody"

def getPosts():
	try:
		# breaking params does not break request
		html = urlopen('http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start=0')
		bs = BeautifulSoup(html, 'lxml')
	except:
		print('request exception - check URL')	

	# question for Ben - is it safe to rely on class names? Or should I search for a pattern in the  structure of child nodes?
	postGroup = bs.find('table', class_='forumline')
	for node in postGroup:
		if (node.name != None):
			idNode = node.find('a', href=re.compile(r'(viewtopic\.php\?p=)\d{5}'))
			if (idNode != None):
				getPostData(node, idNode)
getPosts()

# validate if true for all posts

















