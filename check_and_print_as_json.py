#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pprint
import re
import json
from dw_utilities import *
from adj_street_types import check_street_ending
from adj_postal_code import check_postal_code
from filter_cities import check_city


# In[5]:


osm_file = ".\seattle_map.osm"
json_file = ".\seattle_map.json"


# In[6]:


fp = open(json_file, 'w')    

for x in iterate_elements(osm_file):
    x = check_street_ending(x)
    x = check_postal_code(x)
    if x is not None:
        x = check_city(x)
    if x is not None:
        json.dump(x,fp)
        fp.write('\n')

fp.close()


# In[ ]:




