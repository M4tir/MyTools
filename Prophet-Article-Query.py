# -*- coding: UTF-8 -*- #
import requests
import re
import sys

id = 1
method = sys.argv[1]
content = sys.argv[2]
th='" class="pure-menu-link">'
search_url="https://job.lonelysec.com/xz.aliyun.com"
search=requests.get(url=search_url)
def mstir_search(a,b,string):
    global id
    result = re.findall('.*%s(.*)%s.*'%(a,b),string)
    for x in result:
        if content in x:
            cx=x.replace(th, ' Title:');
            cx=cx.replace('m/', 'm/t/');
            print("===========================================================================")
            print("搜索结果" + str(id) + ":")
            print('Url:http://',cx)
            id = id + 1
def mstir_list(a,b,string):
    result = re.findall('.*%s(.*)%s.*'%(a,b),string)
    for x in result:
        cx=x.replace(th, ' Title:');
        cx=cx.replace('m/', 'm/t/');
        print('Url:http://',cx)
if {method == "list"}:
	print (' ____          __  __     _   _')
	print ('| __ ) _   _  |  \/  |___| |_(_)_ __')
	print ("|  _ \| | | | | |\/| / __| __| | '__|")
	print ("| |_) | |_| | | |  | \__ \ |_| | |")
	print ("|____/ \__, | |_|  |_|___/\__|_|_|")
	print ("       |___/                90sec.com")
	mstir_list('href="/','<',search.text)
if {method == "search"}:
	print (' ____          __  __     _   _')
	print ('| __ ) _   _  |  \/  |___| |_(_)_ __')
	print ("|  _ \| | | | | |\/| / __| __| | '__|")
	print ("| |_) | |_| | | |  | \__ \ |_| | |")
	print ("|____/ \__, | |_|  |_|___/\__|_|_|")
	print ("       |___/                90sec.com")
	mstir_search('href="/','<',search.text)
	print("===========================================================================")