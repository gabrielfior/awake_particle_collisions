# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:22:14 2016

@author: gabrielfior
"""

import ftplib
session = ftplib.FTP('134.107.44.222','gabriel','123')
file = open('energyDeposit.png','rb')                  # file to send
session.storbinary('STOR energyDeposit.png', file)     # send the file
file.close()                                    # close file and FTP
session.quit()