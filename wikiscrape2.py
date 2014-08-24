import urllib2
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/List_of_killings_by_law_enforcement_officers_in_the_United_States,_August_2014'

# Open the HTML file and turn it into a BeautifulSoup object for parsing
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

# The scrape actually starts here. Let's get the table that contains the results.
references = soup.find('ol', attrs={'class': 'references'})

output_lis = [] # The list that's going to store all of our output list items

# First we need to loop through all the list items in the ordered list
for li in references.findAll('li'):

    # And next, we want to get all the text within the list item
    text = li.findAll('span')

    # We'll store all of the values for each given row in a list
    output_text = []
    for span in text:
        output_text.append(span.text.encode('utf-8').strip()) # Delete annoying tab character

    # And we'll add that list to our broader list of results
    output_lis.append(output_text)

# Finally, we'll write our results to a file

print output_lis

handle = open('out3.csv', 'a')
outfile = csv.writer(handle)

outfile.writerows(output_lis)
