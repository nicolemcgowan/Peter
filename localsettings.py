'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "  AC9b3a4af224d6623f4db529c9bf5252dc" 
AUTH_TOKEN = "3a6baa935ad298d322203cfbf33a3067"
PETER_APP_SID = "APa181c44754f00147c2dd1011025c4ee6"
PETER_CALLER_ID = "+14087288937"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
PETER_APP_SID = os.environ['SONYA_APP_SID']
PETER_CALLER_ID = os.environ['SONYA_CALLER_ID']
