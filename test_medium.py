# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:19:37 2016

@author: gabrielfior
"""

from medium import Client

# Go to http://medium.com/me/applications to get your application_id and application_secret.
client = Client(application_id="ed619fa7bd92", application_secret="48f2e217232e2596548faef641082cd045bb4378")

# Build the URL where you can send the user to obtain an authorization code.
#auth_url = client.get_authorization_url("secretstate", "https://yoursite.com/callback/medium",
#                                        ["basicProfile", "publishPost"])

# (Send the user to the authorization URL to obtain an authorization code.)

# Exchange the authorization code for an access token.
#auth = client.exchange_authorization_code("256d00cfce3908d634d99af9fd576fb2670f836e72a5bd33a303420cd80f85c9a",
#                                          "https://yoursite.com/callback/medium")

# The access token is automatically set on the client for you after
# a successful exchange, but if you already have a token, you can set it
# directly.
my_access_token = '2b9d30d98ead9a25dbd5e7530fe22f8a08d771d5e76313e8d27b2588668e434ce'
client.access_token = my_access_token

# Get profile details of the user identified by the access token.
user = client.get_current_user()