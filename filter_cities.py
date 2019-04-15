#!/usr/bin/env python
# coding: utf-8

from dw_utilities import *

def check_city(node):
    e = __city_exists(node)
    if not e:
        return node
    else:
        y = __get_city(node)
        if 'Seattle' in y or 'seattle' in y:
            return node


def __get_city(node):
    city = ''
    x = get_node(node)
    if x is not None:
        for y in x:
            if y.get("tag") is not None:
                if y.get("tag").get("attributes").get("k") == 'addr:city':
                    city = y.get("tag").get("attributes").get("v")
    return city

    
def __city_exists(node):
    exists = False
    x = get_node(node)
    if x is not None:
        for y in x:
            if y.get("tag") is not None:
                if y.get("tag").get("attributes").get("k") == 'addr:city':
                    exists = True
            if exists:
                break
                
    return exists