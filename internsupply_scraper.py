
# coding: utf-8

# In[61]:

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

f = pd.read_csv('/Users/mrudulavysyaraju/PycharmProjects/internships.csv')
internships = f['NextCapital'].tolist() 

website = "http://www.intern.supply/index.html"
page = urllib2.urlopen(website)
soup = BeautifulSoup(page)

companies = []
for cos in soup.find_all(class_ = "alt", id = "companies"):
    for lis in cos.find_all('li'):
        if str(lis.contents[1].text) == 'Apply':
            companies.append(str(lis.contents[0]))
                         
apply_tomorrow = set(companies) - set(internships)
print(apply_tomorrow)
print(len(apply_tomorrow))


# In[ ]:




# In[ ]:



