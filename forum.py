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
# structure of internal page link URL:
# "viewtopic.php?" + param list
# t=[1259] -> topic number
# postdays=[0] -> default 0 for every link. change this and it breaks
# postorder=[asc] -> ascending/descending (dsc)
# start=[0] -> post number
	# a number greater than existing posts does not return error

# method 1 = find nav, find <a> with 'Next'
# method 2 = count # of posts, and use URL' start' param
	# if return does not equal increment amount(15), we're done
	# go one more and check for "No posts exist for this topic" text. if yes, great. if not, exit with error



