import urllib2
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/List_of_killings_by_law_enforcement_officers_in_the_United_States,_August_2014'

# Open the HTML file and turn it into a BeautifulSoup object for parsing
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

# The scrape actually starts here. Let's get the table that contains the results.
only_table = soup.find('table', attrs={'class': 'wikitable sortable'})

output_trs = [] # The list that's going to store all of our output rows

# First we need to loop through all the rows in the table
for tr in only_table.findAll('tr'):

    # And next, we want to get all the cells within each of the rows
    tds = tr.findAll('td')

    # We'll store all of the values for each given row in a list
    output_tds = []
    for td in tds:
        output_tds.append(td.text.encode('utf-8').strip()) # Delete annoying tab character

    # And we'll add that list to our broader list of results
    output_trs.append(output_tds)

# Finally, we'll write our results to a file

print output_trs

handle = open('out2.csv', 'a')
outfile = csv.writer(handle)

outfile.writerows(output_trs)
