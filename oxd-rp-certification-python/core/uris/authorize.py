# File: /oxd-rp-certification-python/core/uris/authorize.py
# Purpose: Act as the /authorize/ path

# Import required modules
import os
import sys
import oxdpython

# Define the test_logic() function
def get_auth_url(oxd_client):
	# Function: get_auth_url()
	# Purpose: Get the OPs authorization URI
	# Arguments:
	#	oxd-client - The oxd client
	
	# Get the authorization URI
	auth_uri = oxd_client.get_authorization_url()
	
	# Return the authorization URI
	return auth_uri
	
	
	
	
