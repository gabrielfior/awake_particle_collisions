# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:45:17 2017

@author: gabrielfior
"""


import urllib
import urllib2

name =  "consultar"
data = {
        "telefone" : %2819%29+99781-6433
       }

http://www.qualoperadora.net/
       
encoded_data = urllib.urlencode(data)
content = urllib2.urlopen("http://www.qualoperadora.net/",
        encoded_data)
print content.readlines()