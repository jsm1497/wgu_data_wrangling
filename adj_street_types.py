#!/usr/bin/env python
# coding: utf-8
import re
from dw_utilities import *

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

street_num_re = re.compile(r'\d{1}\b')

expected = ['Boulevard', 'Lane', 'Court', 'Drive', 'Street','Place','Mall','Plaza','Circle','Road','Point','Way'
            ,'Avenue','North','Northeast','Northwest','South','Southeast','Southwest','East','West','Parkway'
           ,'Loop','Highway']

mapping = { "st": "Street",
            "ave": "Avenue",
            "rd": "Road",
           "pl":"Place",
           "dr":"Drive",
           "ct":"Court",           
           "nw":"Northwest",
           "ne":"Northeast",
           "northest":"Northeast",
           "n":"North",
           "e":"East",
           "w":"West",
           "se":"Southeast",
           's':'South',
           'sw':'Southwest'
            }
            
ordinal = lambda n: "%d%s"%(n,{1:"st",2:"nd",3:"rd"}.get(n if n<20 else n%10,"th"))            

def check_street_ending(node):
    x = node
    c = get_node(x)
    if c is not None:
        for y in c:
            if y.get("tag") is not None:
                if y.get("tag").get("attributes").get("k") == "addr:street":
                    addr = y.get("tag").get("attributes").get("v")
                    #fix street ending
                    addr = __fix_street_ending(addr)
                    
                    #fix other parts in street (middle and beginning of street)
                    if addr:
                        l = addr.split(' ')
                        for i, j in enumerate(l):
                            if l[i].lower() in mapping:
                                l[i] = mapping.get(l[i].lower())
                                
                        addr = " ".join(l)
                        
#removed ordinal indicator due to side effect of adding ordinal indicators to house numbers                        
#                        #fix ordinal indicators
#                        addr = __fix_street_num(addr)
                    
                    #reassign addr to the attribute
                    y.get("tag").get("attributes")["v"] = addr
    return x

def __fix_street_ending(addr):
    m = street_type_re.search(addr)
    if m:
        street_type = m.group()
        y = addr.split(" ")
        y[-1] = re.sub('[^A-Za-z0-9]+', '', y[-1])
        street_type = re.sub('[^A-Za-z0-9]+', '', street_type)
        if y[-1].lower() in mapping:
            y[-1] = mapping.get(y[-1].lower())
            x = " ".join(y)
        else:
            x = addr
        return x
    

#def __fix_street_num(addr):
#    m = street_num_re.search(addr)
#    if m:
#        y = int(m.group()[-1])
#        addr = re.sub(street_num_re,ordinal(y),addr)
#        print(m.group())
#        
#    return addr