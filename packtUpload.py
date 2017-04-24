# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:21:15 2017

@author: gabrielfior
"""

import os
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
from dropbox.client import DropboxClient

TOKEN = 'PG6fJZIM26cAAAAAAAAO6HLG5CTrKQFfIhd06ECrINYfHrEHJqQ8OCqRg2JEZZ7C'

local_directory = '/home/ubuntu/Packtss-books'
dropbox_destination = ''

print("Creating a Dropbox object...")
#dbx = dropbox.Dropbox(TOKEN)
client = DropboxClient(TOKEN)


for root, dirs, files in os.walk(local_directory):

    for filename in files:
        print filename
        # construct the full local path
        local_path = os.path.join(root, filename)

        # construct the full Dropbox path
        relative_path = os.path.relpath(local_path, local_directory)
        dropbox_path = os.path.join(dropbox_destination, relative_path)

        # upload the file
        with open(local_path, 'rb') as f:
            client.put_file(dropbox_path, f)