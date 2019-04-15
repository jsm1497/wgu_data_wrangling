#!/usr/bin/env python
# coding: utf-8

import re
from dw_utilities import *
import pandas as pd

post_code_re = re.compile(r'^\d{5}$')

zip_list_file = ".\seattle_zips.csv"

df = pd.read_csv(zip_list_file)

zips = df.Zipcode.tolist()

# we need to make sure that the list contains strings, not integers
# we use a map function to convert the ints to strings
# this will let the "z not in zips" work properly
zips = list(map(str, zips))


def check_postal_code(node):
    x = node
    y = __get_postal_code(x)
    if y is not None:
        for z in y:
            z = z[0:5]            
            m = post_code_re.search(z)
            if not m or z not in zips:
                return None
    
    return x


def __get_postal_code(node):
    l =[]
    x = get_node(node)
    if x is not None:
        for y in x:
            if y.get("tag") is not None:
                if y.get("tag").get("attributes").get("k") == 'addr:postcode':
                    l.append(y.get("tag").get("attributes").get("v"))
    return l
