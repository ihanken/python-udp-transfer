'''
This file is used as a way to import files a level up in the hierarchy.
'''

import os
import sys
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

# Place any file imports here.

import client
import server
