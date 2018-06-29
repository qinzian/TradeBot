from __future__ import print_function
from sys import stderr

import requests
import json
from lxml import html

def eprint(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

def json_encode(json_obj):
    return json.dumps(json_obj)

def json_decode(json_str):
    return json.loads(json_str)

def sendReceiveReq(url):
    response = sendReq(url)

    # response.content gives the response in bytes
    tree = html.fromstring(response.content)
    #print(response.text)

    jsonResStr = tree.xpath('//a[@class="json_response"]/text()')[0] # there's only 1 item in the returned list from xpath
    #print(jsonResStr)

    return json.loads(jsonResStr) # response as python obj

def sendReq(url):
    #print(url+"\n")
    response = requests.get(url)

    return response
