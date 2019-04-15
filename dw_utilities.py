#!/usr/bin/env python
# coding: utf-8

import xml.etree.cElementTree as ET
from xmljson import cobra as c

tags=('node', 'way', 'relation')
events=('start','end')

def get_node(node):
    if node.get("node") is not None:
        tag_type = "node"
    elif node.get("way") is not None:
        tag_type = "way"
    elif node.get("relation") is not None:
        tag_type = "relation"
    c = node.get(tag_type).get("children")
    if c is not None:
        return c
        

def iterate_elements(osm_file):
    context = ET.iterparse(osm_file, events)
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            x = c.data(elem)
            yield x
        